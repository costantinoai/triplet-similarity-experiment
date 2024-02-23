#!/bin/bash

# Activate the Conda environment
source /home/eik-tb/miniconda3/etc/profile.d/conda.sh
conda activate ml

# Rebuild the Sphinx documentation
sphinx-build -b html -E ./docs/source ./docs/_build

# Create symbolic links to the root folder
ln -sf ./docs/_build/index.html docs.html
ln -sf ./docs/source/introduction.rst README.rst
