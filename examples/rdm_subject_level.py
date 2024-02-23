#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 18:27:31 2023

@author: costantino_ai
"""

# Standard imports
import os

# Local imports
from modules import logging
from modules.analysis.MDS_funcs import apply_dimensionality_reduction_to_activations, MDS_plot
from modules.analysis.rdm_funcs import compute_rdm
from modules.utils.helper_funcs import (
    env_check,
    print_dict,
    OutputLogger,
    create_run_id,
    save_numpy_array,
    extract_model_seed_from_filename,
    load_ordered_dict,
    create_output_directory,
    save_script_to_file,
)

########### PARAMETERS ###########

# Check environment and print info
env_check()

# Define a dictionary to store all parameters for the functions used in the script
params = {
    # General parameters
    "save_logs": True,
    "activations_dir": "./results/20231124-203534_extract-net-activations",
    # Run-specific parameters
    "run_params": {
        "run_id": create_run_id() + "_compute-rdms-subj",
        "reduction_methods": [
            "random_forest"
        ],  # # Dimensionality reduction method ('random_forest', 'PCA', 't-SNE', 'MDS')
        "distance_metric": [
            "pearson"
        ],  # Distance metric for RDM calculation ('pearson', 'mahalanobis', 'euclidean')
    },
    # Parameters specific to dimensionality reduction and RDM computation
    "MDS_plot": {
        "n_components": 2,  # Dimensions for the projection. This needs to be 2 (x,y)
        "alpha": 0.5,  # Transparency level for plot points
        "preprocess": True,  # Preprocess activations like standardization
    },
    "dimensionality_reduction": {
        "n_components": 10,  # Components to retain after reduction
        "preprocess": True,  # Standardize activations before reduction
    },
    "compute_rdm": {
        "rescale": True,  # Rescale RDM to 0-1 range, excluding diagonal
        "plot": True,  # Whether to plot the RDM
    },
}

########### MAIN CODE ###########

# Make output folder and save run files if log is True
out_dir = os.path.join("./results", params["run_params"]["run_id"])
out_text_file = os.path.join(out_dir, "output_log.txt")

# Save script and make output folder
if params["save_logs"]:
    # Make output folder
    create_output_directory(out_dir)

    # Save script to file
    save_script_to_file(out_dir)

    logging.info("Output folder created and script file saved")

with OutputLogger(params["save_logs"], out_text_file):
    print_dict(params)
    # Loop through alll the files in the activations folder
    for file_name in os.listdir(params["activations_dir"]):
        
        # If the file is a pickle file
        if file_name.endswith(".pkl"):
            
            # Load activations data from saved files
            full_path = os.path.join(params["activations_dir"], file_name)
            activations_all_layers = load_ordered_dict(full_path)

            # Extract model, seed info from file name
            model_id, seed = extract_model_seed_from_filename(file_name)

            # Iterating through each layer's activations
            for layer_name, layer_items in activations_all_layers.items():
                
                # For each dimensionality reduction method
                for method in params["run_params"]["reduction_methods"]:
                    
                    # # Perform and plot MDS on the activations
                    # projections = MDS_plot(layer_items, method=method, **params["MDS_plot"])

                    # Apply dimensionality reduction
                    activations_reduced = apply_dimensionality_reduction_to_activations(
                        layer_items, method=method, **params["dimensionality_reduction"]
                    )

                    # for each distance metric in params
                    for distance in params["run_params"]["distance_metric"]:
                        # Compute RDMs
                        rdms = compute_rdm(
                            activations_reduced,
                            layer_name=layer_name,
                            distance_metric=distance,
                            **params["compute_rdm"],
                        )

                        if params["save_logs"]:
                            # Save RDM as a numpy array
                            file_name = f"single-rdms_model-{model_id}_seed-{seed}_layer-{layer_name}_method-{method}_distance-{distance}.npy"
                            save_path = os.path.join(out_dir, file_name)
                            save_numpy_array(rdms, save_path)
