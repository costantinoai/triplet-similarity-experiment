#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 01:26:16 2023

@author: costantino_ai
"""

# Standard imports
import os

# Local imports
from modules import logging
from modules.analysis_funcs.extract_activations_funcs import probe_network_with_stimuli
from modules import device
from modules.net_funcs.dataset_funcs import get_dataloader_from_csv
from modules.net_funcs.net_utils import get_last_level_layer_names, load_alphazero_models
from modules.utils.helper_funcs import (
    OutputLogger,
    create_output_directory,
    create_run_id,
    env_check,
    print_dict,
    save_ordered_dict,
    save_script_to_file,
    set_random_seeds
)


########### PARAMETERS ###########

# Define a dictionary to store all parameters for the functions used in the script
params = {
    
    # General parameters
    "save_logs": True,
    "run_id": create_run_id() + '_extract-net-activations',
    "seeds_num": 1,  # How many different networks we want to initialize and test
    "selected_layers": ["conv", "fc", "relu", "tanh"], # List of strings for activations extraction and plotting
    "reduction_methods": ["random_forest"],  # Dimensionality reduction method ('PCA', 't-SNE', 'MDS')
    "distance_metric": ["pearson"],  # Distance metric for RDM calculation ('pearson', 'mahalanobis', 'euclidean')
    
    # Loading untrained and trained AlphaZeroNet models
    "load_models": {
        "weights_path": "./weights/AlphaZeroNet_20x256.pt",  # Path to trained model weights
        "device": device,  # Computational device (CPU/GPU)
    },  
    
    # Creating a DataLoader for fMRI dataset from a CSV file
    "get_dataloader_from_csv": {
        "csv_file_path": "datasets/fmri_dataset/dataset.csv",  # Path to dataset CSV file
        "batch_size": 40,  # Number of samples per batch
        "shuffle": False,  # Whether to shuffle the dataset
        "num_workers": 8,  # Number of subprocesses for data loading
        "pin_memory": True,  # Copy Tensors into CUDA pinned memory for CUDA GPUs
    },  
    
    # Probing a neural network model with controlled stimuli
    "probe_network_with_stimuli": {
        "device": device,  # Computational device for running the model
    },  
    
    # Visualizing dimensionality reduction of neural network activations
    "MDS_plot": {
        "n_components": 2,  # Dimensions for the projection. This needs to be 2 (x,y)
        "alpha": 0.5,  # Transparency level for plot points
        "preprocess": True,  # Preprocess activations like standardization
    },  
    
    # Applying dimensionality reduction to the activations
    "apply_dimensionality_reduction_to_activations": {
        "n_components": 10,  # Components to retain after reduction
        "preprocess": True,  # Standardize activations before reduction
    },  
    
    # Computing and optionally plotting the RDM for each label
    "compute_rdm": {
        "rescale": True,  # Rescale RDM to 0-1 range, excluding diagonal
        "plot": True,  # Whether to plot the RDM
    },
}

########### MAIN CODE ###########

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
    
    logging.info(f"Starting processing with {params['seeds_num']} seeds.")
    # Set a number of seeds for initialization
    seeds = range(params["seeds_num"])
    
    # Loop through seeds
    for seed in seeds:
        
        logging.debug(f"Processing seed number: {seed}")
        # Set random seeds for reproducibility, ensuring consistent results across runs
        logging.debug("Setting random seeds for reproducibility.")
        set_random_seeds(seed)
    
        logging.info("Loading models...")
        # Load models, both untrained and trained, using specified weight paths and device
        untrained_model, trained_model = load_alphazero_models(**params["load_models"])
        logging.debug("Models loaded successfully.")
    
        logging.debug("Loading data loader from CSV.")
        # Load a data loader from a CSV file, specifying the path to the dataset and the batch size
        data_loader = get_dataloader_from_csv(**params["get_dataloader_from_csv"])
        logging.info("Data loader loaded successfully.")
    
        logging.info("Starting analysis on models.")
        # Analysis parameters
        models = [
            (trained_model, 'trained'),
            (untrained_model, 'untrained')
            ]  # List of models to analyze
    
        # Iterating over the models 
        for model, model_id in models:
            
            # Retrieve names of the last layers in the model
            layers_names_all = get_last_level_layer_names(model)
    
            # Filter the layer names based on the selected layers
            layers_names = [
                layer_name
                for layer_name in layers_names_all
                if any(sel_layer in layer_name for sel_layer in params["selected_layers"])
            ]
    
            logging.debug(f"Probing network for model '{model_id}' with stimuli.")
            # Probe the network with stimuli and get activations for the specified layers
            activations_all_layers = probe_network_with_stimuli(
                model, layers_names, data_loader, **params["probe_network_with_stimuli"]
            )
            logging.info(f"Completed probing for model '{model_id}'.")

            if params["save_logs"]:
                # Save dictionary to file
                pkl_path = os.path.join(out_dir, f'activations_model-{model_id}_seed-{seed}.pkl')
                logging.debug(f"Saving activations to file: {pkl_path}")
                save_ordered_dict(activations_all_layers, pkl_path)
                logging.info(f"Activations saved successfully for model '{model_id}', seed {seed}.")
                    