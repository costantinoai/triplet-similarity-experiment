#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 13:45:47 2023

@author: costantino_ai
"""
import numpy as np
from scipy.spatial.distance import pdist, squareform
from sklearn.covariance import MinCovDet
import matplotlib.pyplot as plt

def safe_normalize_rdm(rdm):
    """
    Safely normalizes the representational dissimilarity matrix (RDM).

    This function normalizes the RDM by adjusting its values to a 0-1 scale based on the maximum and minimum values
    in its upper or lower triangle (excluding the diagonal). If normalization is not possible, it returns the original RDM.

    :param rdm: The representational dissimilarity matrix to normalize.
    :type rdm: np.ndarray
    :returns: The normalized RDM if possible, otherwise returns the original RDM.
    :rtype: np.ndarray
    """
    try:
        # Ensure the RDM is not empty
        if rdm.size == 0:
            raise ValueError("RDM is empty.")

        # Use the values of the lower triangle, excluding the diagonal
        lower_triangle_values = rdm[np.tril_indices(rdm.shape[0], k=-1)]

        # Check if the lower triangle values are not all the same
        if np.all(lower_triangle_values == lower_triangle_values[0]):
            raise ValueError("All elements in RDM lower triangle are the same.")

        # Normalize using the lower triangle values
        max_val = np.max(lower_triangle_values)
        min_val = np.min(lower_triangle_values)
        normalized_rdm = (rdm - min_val) / (max_val - min_val)
        return normalized_rdm

    except ValueError as e:
        # Log the error and return the original RDM
        print(f"Error in RDM normalization: {e}")
        return rdm

def calculate_mahalanobis_distance(activations_np):
    """
    Calculate the Mahalanobis distances of given observations.

    The Mahalanobis distance is a measure of the distance between a point and a distribution.
    It is an effective way to determine similarity between an unknown sample and a known one.
    This function calculates these distances using the minimum covariance determinant for
    robustness against outliers.

    :param activations_np: A 2D numpy array where each row represents an observation
                           and each column represents a variable.
    :type activations_np: numpy.array
    :returns: A 1D array of Mahalanobis distances of each observation from the group.
    :rtype: numpy.array
    :raises ValueError: If the input is not a 2D numpy array or has less than 2 columns.
    """
    # Validate input
    if not isinstance(activations_np, np.ndarray) or len(activations_np.shape) != 2 or activations_np.shape[1] < 2:
        raise ValueError("Input must be a 2D numpy array with at least 2 variables (columns).")

    try:
        # Fit the Minimum Covariance Determinant estimator to the data
        cov = MinCovDet().fit(activations_np)

        # Calculate Mahalanobis distance using the robust covariance estimate
        distances = pdist(activations_np, metric="mahalanobis", VI=cov.covariance_)
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating distances: {e}")

    return distances

def compute_rdm(probe_output, n_components=None, distance_metric="euclidean", rescale=True, plot=False, layer_name=''):
    """
    Compute and optionally plot the RDM for each label using the specified distance metric,
    excluding the diagonal when rescaling.

    :param probe_output: Output from the probe_network_with_stimuli function.
    :type probe_output: dict
    :param n_components: Number of components to retain after dimensionality reduction, or None to use all components.
    :type n_components: int, optional
    :param distance_metric: Distance metric ('euclidean', 'mahalanobis', or 'pearson').
    :type distance_metric: str
    :param rescale: Rescale RDM to 0-1 range if True, excluding the diagonal.
    :type rescale: bool
    :param plot: Plot the RDM if True.
    :type plot: bool
    :param layer_name: Name of the layer for which the RDM is computed, used in plotting.
    :type layer_name: str
    :returns: Dictionary with labels as keys and corresponding RDMs as values.
    :rtype: dict
    """
    # Process each activation as an independent observation
    activations_np = np.array([probe_output[stim_id]['activation'] for stim_id in probe_output.keys()])
    
    # Flatten the activations 
    activations_np = activations_np.reshape(activations_np.shape[0], -1)
    
    # stim_ids = tuple(probe_output.keys())
    strategies = tuple(int(probe_output[stim_id]['strategy']) for stim_id in probe_output.keys())

    # Compute pairwise distances based on the specified metric
    if activations_np.shape[1] == 1 or distance_metric == "euclidean":
        distances = pdist(activations_np, metric="euclidean")
    elif distance_metric == "mahalanobis":
        distances = calculate_mahalanobis_distance(activations_np)
    elif distance_metric == "pearson":
        distances = pdist(activations_np, metric=lambda u, v: 1 - np.corrcoef(u, v)[0, 1])
    else:
        raise ValueError("Invalid distance metric specified.")

    rdm = squareform(distances)

    # Rescale RDM to 0-1 range, excluding the diagonal
    if rescale:
        rdm = safe_normalize_rdm(rdm)

    # Set the diagonal to zero
    np.fill_diagonal(rdm, 0)

    # Plotting the RDM
    if plot:
        plt.figure(figsize=(8, 6))
        plt.imshow(rdm, cmap="viridis")
        plt.colorbar()
        plt.title(f"RDM using {distance_metric} - {layer_name}")

        # Modify the x-ticks
        ticks = []
        tick_labels = []

        # Initialize the previous label for comparison
        prev_label = None

        # Iterate through all labels
        for i, label in enumerate(strategies):
            # Check if the current label is different from the previous one
            if label != prev_label:
                # Add the index to ticks and the label to tick_labels
                ticks.append(i)
                tick_labels.append(label)
            # Update the previous label
            prev_label = label

        plt.xticks(ticks, labels=tick_labels, fontsize=8)
        plt.yticks(ticks, labels=tick_labels, fontsize=8)

        plt.xlabel("Observations")
        plt.ylabel("Observations")
        plt.show()

    return rdm
