#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
Created on	Fri Feb 23 16:13:00 2024

@Author  :   tvhgn
'''

# Standard imports
from itertools import combinations
import random
import os

import pandas as pd
import numpy as np

########### PARAMETERS ###########
# Create list of 'num' scenarios
num = 40
prop_train = 0.9 # proportion of dataset allocated to training data

########### MAIN CODE ###########

scenarios = [i for i in range(1, num+1, 1)]

# Generate all possible triplets and shuffle the list
np.random.seed(42)
triplets = np.asarray(list(combinations(scenarios, 3)))

# Initialize a set to keep track of the unique combinations
unique_triplets_set = set()

# Filter out non-unique combinations
for triplet in triplets:
    # Sort the tuple to ensure that permutations are treated as the same
    sorted_triplet = tuple(sorted(triplet))
    # Add to the set (this automatically filters out duplicates)
    unique_triplets_set.add(sorted_triplet)

# Convert the set back to a list of triplets
unique_triplets = np.asarray(list(unique_triplets_set))

# Shuffle the list if necessary
np.random.shuffle(unique_triplets)
n = unique_triplets.shape[0]
split_idx = round(prop_train*n)

# Split the data
train_data = unique_triplets[:split_idx]
test_data = unique_triplets[split_idx:]
data = [unique_triplets, train_data, test_data] # Combine into single list

# Create text files for training data and test data separately
base_path = os.path.join("test", "test_results", "triplets", "dataset")
train_path = os.path.join(base_path, "train_90.npy")
test_path = os.path.join(base_path, "test_10.npy")
all_path = os.path.join(base_path, "all_triplets.npy")

for i, path in enumerate([all_path, train_path, test_path]):
    with open(path, 'wb') as file:
        np.save(file, data[i], allow_pickle=False)
    
# Show message upon completion.
print(f"\nDummy data generated and stored in {path}!\n")