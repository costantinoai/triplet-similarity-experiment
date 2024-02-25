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
num_triplets = 1000

########### Main Code ###########
# Read stimuli from datset file
df = pd.read_csv('test\dataset.csv') 
stimuli = df['imageName'].to_numpy()

triplets = []
triplets_set = set()  # Use a set to track unique triplets

# Generate triplets
while len(triplets) < num_triplets:
    # Generate a new triplet
    triplet = np.random.choice(stimuli, size=3, replace=False)
    triplet_tuple = tuple(sorted(triplet))  # To be used for tracking duplicates

    # Check if the sorted triplet is not already in the set before appending
    if triplet_tuple not in triplets_set:
        triplets.append(list(triplet))  # Append the original triplet list
        triplets_set.add(triplet_tuple)  # Add the sorted tuple to the set for future checks

  
# Create dataframe from list
df = pd.DataFrame(data=triplets,
                  columns=["Stim1", "Stim2", "Stim3"])

# Save to csv file
df.to_csv(r"test\triplets.csv", index=False)