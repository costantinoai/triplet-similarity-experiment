#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 01:45:55 2023

@author: costantino_ai
"""
import torch

from modules import logging
from copy import deepcopy

from modules.models.alphazero.AlphaZeroNetwork import AlphaZeroNet as az_net
from modules.net_funcs.net_utils import initialize_weights

def load_alphazero_models(weights_path="./weights/AlphaZeroNet_20x256.pt", device='cpu'):
    """
    Loads and returns an untrained and a trained AlphaZeroNet model.

    :param weights_path: Path to the file containing the trained model weights. 
                         Default is './weights/AlphaZeroNet_20x256.pt'.
    :type weights_path: str
    :param device: The device on which the models are loaded. Default is 'cpu'.
    :type device: str
    :returns: A tuple containing the untrained and trained AlphaZeroNet models.
    :rtype: tuple
    :raises FileNotFoundError: If the weights file specified by weights_path is not found.

    :Example:

    >>> untrained_model, trained_model = load_alphazero_models()

    Note:
    - The function assumes that the AlphaZeroNet model and the necessary libraries are already imported and available in the environment where this function is used.
    - The trained model is loaded with weights from the specified path, while the untrained model does not have any pre-loaded weights.
    """
    # Initialize untrained AlphaZeroNet model and move to device
    untrained_model = az_net(20, 256)
    initialize_weights(untrained_model)
    untrained_model = untrained_model.to(device)
    untrained_model.eval()  # Set model to evaluation mode

    if weights_path != None:
        # Create a deep copy of the untrained model for the trained model
        trained_model = deepcopy(untrained_model)
        try:
            # Load weights into the trained model
            checkpoint = torch.load(weights_path, map_location=device)
            trained_model.load_state_dict(checkpoint)
            trained_model.to(device)  # Move trained model to the device
            trained_model.eval()  # Set trained model to evaluation mode
        except FileNotFoundError:
            raise FileNotFoundError(f"Weights file not found at '{weights_path}'. Please check the file path.")
        return untrained_model, trained_model
    else:
        logging.log("No 'weights_path' passed to load_models. Returning untrained model only.")
        return untrained_model
