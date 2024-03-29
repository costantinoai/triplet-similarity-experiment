#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Created on	Fri Feb 23 16:13:00 2024

@Author  :   tvhgn
'''

# Standard 
from itertools import combinations
import os
import sys
sys.path.append(os.getcwd()) # Necessary to get it working on my setup
sys.path.append(os.path.abspath("modules"))
# 3rd party
import pandas as pd
import numpy as np
# local
from modules import logging
from modules.helper_funcs.utils import (
    OutputLogger,
    create_output_directory,
    create_run_id,
    print_dict,
    save_script_to_file,
    set_random_seeds
)
from modules.net_funcs.net_utils import env_check

########### PARAMETERS ###########
# Define a dictionary to store all parameters for the functions used in the script
params = {
    # General parameters
    "save_logs": True,
    "run_id": create_run_id() + '_extract-net-activations',
    "seed": 42,
    
    # Functions-specific parameters
    "num": 40, # For creating list of num scenarios
    "prop_train": 0.9 # proportion of dataset allocated to training data
}

########### MAIN CODE ###########
set_random_seeds(params["seed"])

# Make output folder and save run files if log is True
out_dir = os.path.join("./results", params["run_id"])
out_text_file = os.path.join(out_dir, "output_log.txt")

# Save script and make output folder
if params["save_logs"]:
    
    # Make output folder
    create_output_directory(out_dir)
    
    # Save script to file
    save_script_to_file(out_dir)

    logging.info("Output folder created and script file saved")

with OutputLogger(params["save_logs"], out_text_file):
    # Check environment and print info
    env_check()

    # Printing run info and device information
    print_dict(params)
    
    logging.info("Started processing.")
    
    #### DUMMY DATA CODE ####
    
    scenarios = [i for i in range(1, params["num"], 1)]

    # Generate all possible triplets and shuffle the list
    np.random.seed(42)
    triplets = np.asarray(list(combinations(scenarios, 3)))

    # Initialize a set to keep track of the unique combinations
    unique_triplets_set = set()

    # Filter out non-unique combinations
    for triplet in triplets:
        # Sort the tuple to ensure that permutations are treated as the same
        sorted_triplet = tuple(sorted(triplet))
        # Add to the set (this automatically filters out duplicates)
        unique_triplets_set.add(sorted_triplet)

    # Convert the set back to a list of triplets
    unique_triplets = np.asarray(list(unique_triplets_set))

    # Shuffle the list if necessary
    np.random.shuffle(unique_triplets)
    n = unique_triplets.shape[0]
    split_idx = round(params['prop_train']*n)

    # Split the data
    train_data = unique_triplets[:split_idx]
    test_data = unique_triplets[split_idx:]
    data = [unique_triplets, train_data, test_data] # Combine into single list

    # Create text files for training data and test data separately
    base_path = os.path.join("test", "test_results", "triplets", "dataset")
    train_path = os.path.join(base_path, "train_90.npy")
    test_path = os.path.join(base_path, "test_10.npy")
    all_path = os.path.join(base_path, "all_triplets.npy")
    
    # Store data in .npy format
    for i, path in enumerate([all_path, train_path, test_path]):
        with open(path, 'wb') as file:
            np.save(file, data[i], allow_pickle=False)
        
    # Show message upon completion.
    print(f"\nDummy data generated and stored in {path}!\n")

    ########################
    
    logging.info("Completed processing.")

    if params["save_logs"]:
        
        # Save data to file        
        pass # TODO: ADD YOUR SAVING CODE HERE                    


