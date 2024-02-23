#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:20:18 2023

@author: costantino_ai
"""

# Standard imports
import os

# Local imports
from modules import logging
from modules.utils.helper_funcs import (
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
    "seed": 42
    
    # Functions-specific parameters
    # TODO: add parameters for each function in the main code
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
    
    # TODO: ADD YOUR MAIN CODE HERE
    
    logging.info("Completed processing.")

    if params["save_logs"]:
        # Save data to file        
        pass # TODO: ADD YOUR SAVING CODE HERE                    
