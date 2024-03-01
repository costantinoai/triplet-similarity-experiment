#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Created on	Sun Feb 25 16:04:31 2024

@Author  :   tvhgn
'''

# Standard imports
import os

import numpy as np
import pandas as pd

########### PARAMETERS ###########
triplets_n = 9880 # Max number of unique triplets possible from 40 total scenario's

########### Main Code ###########
# Read stimuli from datset file
df = pd.read_csv('test\dataset.csv') 
stimuli = df['imageName'].to_numpy()

# Initialize variables
triplets = []
triplets_set = set()  # Use a set to track unique triplets

# Generate triplets
while len(triplets) < triplets_n:
    # Generate a new triplet
    triplet = np.random.choice(stimuli, size=3, replace=False)
    triplet_tuple = tuple(sorted(triplet))  # To be used for tracking duplicates

    # Check if the sorted triplet is not already in the set before appending
    if triplet_tuple not in triplets_set:
        triplets.append(list(triplet))  # Append the original triplet list
        triplets_set.add(triplet_tuple)  # Add the sorted tuple to the set for future checks

# Create dataframe from list
df_triplets = pd.DataFrame(data=triplets,
                  columns=["Stim1", "Stim2", "Stim3"])

# Create filepath
filepath = os.path.join("test", "triplets.csv")

# Save to csv file
df_triplets.to_csv(filepath, index=False)
