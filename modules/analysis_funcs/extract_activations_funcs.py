#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:06:31 2023

@author: costantino_ai
"""
import math
import os
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from modules import logging
from modules.net_funcs.net_utils import freeze_layers, print_model_summary, plot_layer_activations
from modules.helper_funcs.utils import sort_ordered_dict_by_key

def get_layer_activation(model, layer_names, position, mask):
    """
    Get the activations of specified layers in response to input data.

    :param model: The neural network model to probe.
    :type model: torch.nn.Module
    :param layer_names: List of names of the layers to probe.
    :type layer_names: list
    :param position: Position tensor.
    :type position: tensor
    :param mask: Mask tensor.
    :type mask: tensor
    :returns: A dictionary where keys are layer names and values are corresponding activations.
    :rtype: dict
    """
    # Ensure layer_names is a list
    if not isinstance(layer_names, list):
        layer_names = [layer_names]

    # Hook for extracting activations
    activations = {name: None for name in layer_names}
    hooks = []

    def get_activation(name):
        def hook(model, input, output):
            activations[name] = output.detach()
        return hook

    # Register hooks for each layer
    for name in layer_names:
        layer = dict([*model.named_modules()])[name]
        hook = layer.register_forward_hook(get_activation(name))
        hooks.append(hook)

    # Forward pass
    model(position, policyMask=mask)

    # Remove the hooks
    for hook in hooks:
        hook.remove()

    # Return the activations for the specified layers
    return activations

def probe_network_with_stimuli(model, layer_names, stimuli_loader, device):
    """
    Probes a neural network model with controlled stimuli and extracts activations for specified layers.

    This function iterates through a DataLoader containing stimuli, applies these stimuli to a neural network model,
    and extracts activations from specified layers. The activations along with the original stimuli information are
    stored in an OrderedDict. Each key in this dictionary is a layer name, and each value is another OrderedDict,
    keyed by 'stim_id', containing stimuli information and corresponding activations for that layer.

    :param model: The neural network model to probe. It should be in evaluation mode.
    :type model: torch.nn.Module
    :param layer_names: A list of string names representing the layers to probe in the model.
    :type layer_names: list
    :param stimuli_loader: A DataLoader containing the stimuli to be applied to the model.
    :type stimuli_loader: torch.utils.data.DataLoader
    :param device: The computational device (e.g., CPU or CUDA) on which to run the model.
    :type device: torch.device
    :returns: A dictionary where each key is a layer name, and each value is an OrderedDict of stimuli (keyed by 'stim_id') and activations.
    :rtype: collections.OrderedDict
    """
    # Set the model to evaluation mode. This is crucial as it disables layers like dropout and batch normalization.
    model.eval()
    model = freeze_layers(model)
    print_model_summary(model, input_shape=[(1, 16, 8, 8), (1, 72, 8, 8)])
    
    # Initialize an empty OrderedDict to store activations by layer.
    stimuli_dict_by_layer = OrderedDict()

    # Iterate over each batch in the stimuli DataLoader.
    for batch_index, stimuli_dict in enumerate(stimuli_loader):
        logging.info(f"Processing batch {batch_index + 1}")

        # Extract positions and masks, and move them to the specified device (CPU/GPU).
        positions = stimuli_dict['position'].to(device)
        masks = stimuli_dict['mask'].to(device)

        # Extract the layer activations for the given batch of stimuli using the provided model.
        layers_activations = get_layer_activation(model, layer_names, positions, masks)

        # Process each layer's activations.
        for layer, activations in layers_activations.items():
            # For each layer, either get the existing OrderedDict or create a new one.
            layer_data = stimuli_dict_by_layer.setdefault(layer, OrderedDict())

            # Iterate over each activation in the current layer.
            for i, activation in enumerate(activations):
                # Extract the stimulus ID for the current activation.
                stim_id = stimuli_dict['stim_id'][i].item()

                # Create a dictionary for the current stimulus, copying all relevant information from the original stimuli_dict.
                stimulus_info = {key: stimuli_dict[key][i] for key in stimuli_dict}

                # Add the activation data to the stimulus information.
                stimulus_info['activation'] = activation.cpu().numpy()

                # Store the stimulus information in the layer data, keyed by stim_id.
                layer_data[stim_id] = stimulus_info

    # Sort the data in each layer's dictionary by stim_id using the sort_ordered_dict_by_key function.
    for layer in stimuli_dict_by_layer:
        stimuli_dict_by_layer[layer] = sort_ordered_dict_by_key(stimuli_dict_by_layer[layer])

    logging.info("Processing complete.")
    return stimuli_dict_by_layer

def plot_activations_from_probe_output(probe_output, stim_id, image_folder='datasets/fmri_dataset/images'):
    """
    Plot the original image and the activations for a specific image given its stim_id.

    :param probe_output: The output from probe_network_with_stimuli function.
                         Expected to contain information about each stimulus and its activations.
    :type probe_output: dict
    :param stim_id: The stimulus identifier for which the activations and image will be plotted.
    :type stim_id: int
    :param image_folder: The folder where images are stored. Defaults to 'datasets/fmri_dataset/images'.
    :type image_folder: str, optional
    """
    # Function body...
    if stim_id in probe_output:
        activations = probe_output[stim_id]['activation']
        filename = probe_output[stim_id]['filename']

        # Construct the full path of the image
        image_path = os.path.join(image_folder, filename)

        # Load the image
        image = np.array(Image.open(image_path))

        # Calculate the grid size (as square as possible)
        num_cols = int(math.ceil(math.sqrt(activations.shape[0])))
        num_rows = int(math.ceil(activations.shape[0] / num_cols))

        # Plot the original image
        plt.figure(figsize=(num_cols * 2, num_rows * 2))
        plt.imshow(image)
        plt.axis("off")
        plt.title(f"Original Image: {stim_id}")
        plt.show()

        # Plot the activations
        plot_layer_activations(activations, num_cols)
    else:
        print("Specified stim_id not found in the probe output.")

