#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:08:04 2023

@author: costantino_ai
"""
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from copy import deepcopy
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import MDS, TSNE
from sklearn.preprocessing import StandardScaler

from modules import logging

def apply_dimensionality_reduction_to_activations(activations, n_components, method="PCA", preprocess=True):
    """
    Applies dimensionality reduction to the activations in the given dictionary.

    :param activations: Dictionary with stim_id as keys and dictionaries containing 'activation' data.
    :type activations: dict
    :param n_components: Number of components to retain after reduction.
    :type n_components: int
    :param method: Reduction method ('random_forest', 'PCA', 't-SNE', 'MDS'). Default is 'PCA'.
    :type method: str
    :param preprocess: Whether to standardize activations before reduction. Default is True.
    :type preprocess: bool
    :returns: Dictionary with updated 'activation' data post reduction.
    :rtype: dict
    :raises ValueError: For invalid `n_components`, method, or input dictionary structure.
    """
    
    # Validate n_components and method inputs
    if not isinstance(n_components, int) or n_components <= 0:
        raise ValueError("n_components must be a positive integer.")
    if method not in ["PCA", "t-SNE", "MDS", "random_forest"]:
        raise ValueError("Invalid method. Choose 'random_forest', 'PCA', 't-SNE', or 'MDS'.")

    # Ensure the input structure is correct
    if not all('activation' in v for v in activations.values()):
        raise ValueError("Each entry in activations must contain an 'activation' key.")

    # Prepare data for dimensionality reduction
    try:
        # Extract and flatten activations into a list
        flattened_activations = [v['activation'].reshape(-1) for v in activations.values()]
    except Exception as e:
        logging.error(f"Error processing activations: {e}")
        raise

    # Stack flattened activations into a 2D NumPy array
    activations_np = np.vstack(flattened_activations)

    # Optionally preprocess the data
    if preprocess and method in ["PCA", "t-SNE"]:
        scaler = StandardScaler()
        activations_np = scaler.fit_transform(activations_np)

    # Initialize and apply the chosen dimensionality reduction method
    try:
        if method == "PCA":
            reducer = PCA(n_components=n_components, random_state=42, svd_solver='auto')
        elif method == "t-SNE":
            reducer = TSNE(n_components=2, random_state=42)
        elif method == "MDS":
            reducer = MDS(n_components=n_components, random_state=42)
        elif method == "random_forest":
            # Fit a model to the data
            model = RandomForestClassifier(random_state=42)

        # Check if reduction is applicable
        if method == "random_forest":
            Y = np.arange(0, len(activations_np))
            model.fit(activations_np, Y)
            
            # Select 500 most informative features
            selector = SelectFromModel(model, max_features=n_components, prefit=True)
            activations_reduced = selector.transform(activations_np)
        else:
            if activations_np.shape[1] >= n_components:
                activations_reduced = reducer.fit_transform(activations_np)
            else:
                logging.warning("Number of features is less than n_components. Returning original activations.")
                return deepcopy(activations)

    except Exception as e:
        logging.error(f"Error applying dimensionality reduction: {e}")
        raise

    # Update the activations in the original dictionary
    transformed_activations = deepcopy(activations)
    for i, stim_id in enumerate(activations):
        transformed_activations[stim_id]['activation'] = activations_reduced[i]

    return transformed_activations

def MDS_plot(probe_output, method="MDS", n_components=2, alpha=0.5, preprocess=True):
    """
    Visualize dimensionality reduction of neural network activations.

    This function applies random_forest, PCA, t-SNE, or MDS to the activations from the probe_output
    and plots the results in 1D, 2D, or 3D. It is used to understand the distribution of
    neural activations across different labels or strategies.

    :param probe_output: A dictionary with labels as keys and lists of numpy arrays (activations) as values.
    :type probe_output: dict
    :param method: The dimensionality reduction method ('PCA', 't-SNE', or 'MDS').
    :type method: str
    :param n_components: Number of dimensions for the projection (1, 2, or 3).
    :type n_components: int
    :param alpha: Transparency level for the plot points.
    :type alpha: float
    :param preprocess: Whether to apply preprocessing like standardization.
    :type preprocess: bool
    :returns: A dictionary of projections with each key as a label and value as the reduced dimensionality data.
    :rtype: dict
    """
    # Check if n_components is either 2 or 3
    if n_components not in [2, 3]:
        raise ValueError("n_components must be either 2 or 3.")

    # Check if only one feature is present in the activations
    if len(probe_output[list(probe_output.keys())[0]]['activation'].shape) == 1:
        # Warn the user and adjust n_components to 1 if only one feature is detected
        logging.warning("Only one feature detected. Adjusting to 1D projection.")
        proj = probe_output
        n_components = 1

    # Apply dimensionality reduction to the activations
    proj = apply_dimensionality_reduction_to_activations(
        probe_output, n_components, method=method, preprocess=preprocess
    )

    # Create a figure for plotting
    fig = plt.figure(figsize=(8, 6))

    # Extract the unique categories (strategies) from the data
    categories = [int(stim_dict['strategy']) for _, stim_dict in proj.items()]
    # unique_categories = set(categories)

    # Select the appropriate plotting method based on the number of dimensions
    if n_components == 1:
        plot_1d_data(proj, categories, alpha)
    elif n_components == 2:
        plot_2d_data(proj, categories, method, alpha)
    elif n_components == 3:
        plot_3d_data(proj, categories, method, alpha, fig)

    # Display the legend and show the plot
    plt.legend()
    plt.show()

    return proj

def plot_1d_data(proj, categories, alpha):
    """
    Plot 1D data with random y-axis offsets for visualization.

    :param proj: Projected data points.
    :type proj: dict
    :param categories: Categories or labels for the data points.
    :type categories: list or similar iterable
    :param alpha: Transparency level for the plot points.
    :type alpha: float
    """
    for strategy in set(categories):
        # Get the projected points for the current strategy
        projected_points = np.array([proj[stim_id]['activation'] for stim_id in proj if proj[stim_id]['strategy'] == strategy])
        # Create random offsets along the y-axis for better visualization
        y_offsets = np.random.uniform(-0.01, 0.01, size=projected_points.shape[0])
        # Plot the points with the specified alpha (transparency)
        plt.scatter(projected_points.flatten(), y_offsets, alpha=alpha, label=f"Strategy {strategy}")
    plt.title("Analysis with Single Feature")
    plt.ylabel("Activation Value")
    plt.xlabel("Random Offset")

def plot_2d_data(proj, categories, method, alpha):
    """
    Plot 2D data with appropriate labels and titles.

    :param proj: Projected data points.
    :type proj: dict
    :param categories: Categories or labels for the data points.
    :type categories: list or similar iterable
    :param method: The dimensionality reduction method used.
    :type method: str
    :param alpha: Transparency level for the plot points.
    :type alpha: float
    """
    plt.xlabel(f"{method} Dim 1")
    plt.ylabel(f"{method} Dim 2")
    plt.title(f"Dimensionality Reduction Analysis using {method}")
    for strategy in set(categories):
        # Get the projected points for the current strategy
        projected_points = np.array([proj[stim_id]['activation'] for stim_id in proj if proj[stim_id]['strategy'] == strategy])
        # Plot the points in 2D space
        plt.scatter(projected_points[:, 0], projected_points[:, 1], alpha=alpha, label=f"Strategy {strategy}")

def plot_3d_data(proj, categories, method, alpha, fig):
    """
    Plot 3D data with appropriate axis labels and titles.

    :param proj: Projected data points.
    :type proj: dict
    :param categories: Categories or labels for the data points.
    :type categories: list or similar iterable
    :param method: The dimensionality reduction method used.
    :type method: str
    :param alpha: Transparency level for the plot points.
    :type alpha: float
    :param fig: The figure object on which the 3D plot will be drawn.
    :type fig: matplotlib.figure.Figure
    """
    ax = fig.add_subplot(111, projection="3d")
    ax.set_xlabel(f"{method} Dim 1")
    ax.set_ylabel(f"{method} Dim 2")
    ax.set_zlabel(f"{method} Dim 3")
    plt.title(f"Dimensionality Reduction Analysis using {method}")
    for strategy in set(categories):
        # Get the projected points for the current strategy
        projected_points = np.array([proj[stim_id]['activation'] for stim_id in proj if proj[stim_id]['strategy'] == strategy])
        # Plot the points in 3D space
        ax.scatter(projected_points[:, 0], projected_points[:, 1], projected_points[:, 2], alpha=alpha, label=f"Strategy {strategy}")
