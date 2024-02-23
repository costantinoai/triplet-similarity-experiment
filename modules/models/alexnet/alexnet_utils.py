#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 25 01:43:00 2023

@author: costantino_ai
"""

import torch
import torch.nn as nn
from torchvision import models
from copy import deepcopy
from modules import logging

def load_alexnet_mnist(weights_path=None, device='cpu'):
    """
    Loads and returns an untrained and an optionally trained AlexNet model for MNIST.

    This function initializes an untrained AlexNet model and optionally loads weights for a trained model.
    It returns both the untrained and trained models. The models are loaded onto the specified device.

    :param weights_path: Path to the file containing the trained model weights. 
                         Default is None, which means no weights are loaded.
    :type weights_path: str, optional
    :param device: The device to load the model onto ('cpu' or 'cuda'). Default is 'cpu'.
    :type device: str
    :returns: A tuple containing the untrained and optionally trained AlexNet models.
    :rtype: tuple
    :raises FileNotFoundError: If the weights file specified by weights_path is not found.

    :Example:

    >>> untrained_model, trained_model = load_alexnet_mnist('./weights/alexnet_mnist.pt')
    """

    # Initialize untrained AlexNet model
    untrained_model = models.alexnet(pretrained=False)
    in_feat = untrained_model.classifier[-1].in_features
    untrained_model.classifier[-1] = nn.Linear(in_features=in_feat, out_features=10, bias=True)
    untrained_model = untrained_model.to(device)
    untrained_model.eval()  # Set model to evaluation mode

    if weights_path:
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
        logging.info("No 'weights_path' passed to load_alexnet_mnist. Returning untrained model only.")
        return untrained_model, None