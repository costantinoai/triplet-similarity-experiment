#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Created on	Fri Feb 23 16:13:00 2024

@Author  :   tvhgn
'''

# Standard 
from itertools import combinations
import random
import os

import pandas as pd
import numpy as np

from modules import logging
from modules.helper_funcs import (
    OutputLogger,
    create_output_directory,
    create_run_id,
    env_check,
    print_dict,
    save_script_to_file,
    set_random_seeds
)

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
    triplets = np.asarray(list(combinations(scenarios, 3)))
    np.random.shuffle(triplets)
    n = triplets.shape[0]
    split_idx = round(params["prop_train"]*n)

    # Split the data
    train_data = triplets[:split_idx]
    test_data = triplets[split_idx:]

    # Create text files for training data and test data separately
    path = os.path.join("test_results", "triplets", "dataset")
    train_path = os.path.join(path, "train_90.npy")
    test_path = os.path.join(path, "test_10.npy")
    # np.savetxt(train_path, train_data, fmt="%d", delimiter=',')
    # np.savetxt(test_path, test_data, fmt="%d", delimiter=',')
    np.save(train_path, train_data, allow_pickle=False)
    np.save(test_path, test_data, allow_pickle=False)

    ########################
    
    logging.info("Completed processing.")

    if params["save_logs"]:
        
        # Save data to file        
        pass # TODO: ADD YOUR SAVING CODE HERE                    


