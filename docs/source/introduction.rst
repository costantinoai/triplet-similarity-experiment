.. _introduction:

Introduction
============

Welcome to the Triplets Similarity Experiment repository!
------------------------------------------------------------------

This repository serves as a versatile starting point for your deep learning and neuroscience projects. This template provides a solid foundation for building, training, and analyzing neural networks and conducting neuroscience experiments.

Key Features
------------

- **Modular Architecture**: The template follows a modular design, making it easy to organize and manage your code for different project components.

- **Data Handling**: Efficient data handling utilities are included, enabling you to preprocess, augment, and load datasets effortlessly.

- **Analysis Tools**: Tools for analyzing neural network activations, conducting dimensionality reduction, and visualizing results are readily available.

- **Documentation**: Clear and comprehensive documentation helps you get started quickly and navigate through the project effortlessly.

Project Structure
-----------------

This simplified structure helps keep your project organized and maintainable:

- ``datasets/``: Store your datasets. For example, an "fmri_dataset" directory contains a sample CSV dataset and image files.
- ``docs/``: The documentation files. To open the documentation, open `./docs/_build/index.html`.
- ``examples/``: Explore sample projects to understand how to structure your own.
- ``modules/``: Contains Python modules for different functionalities. Subdirectories represent different modules.
- ``results/``: This folder can be used to store any results or outputs generated during experiments.
- ``test/``: Store your unfinished/untested scripts.

Modules Overview
----------------

The Deep Learning and Neuroscience Template Repository is organized into several modules to facilitate code organization and modularity:

- ``modules.analysis_funcs``: Contains functions for analyzing neural network activations and conducting related analyses.

- ``modules.helper_funcs``: Provides utility functions that are useful throughout your project.

- ``modules.models``: Includes model-related code, such as neural network architectures and training configurations.

- ``modules.net_funcs``: Contains functions for dataset handling, network utilities, and training/testing procedures.

Each module serves a specific purpose, making it easier to navigate and work with the template for your projects.

You can find detailed documentation for each module in the respective sections.

Installation
============

Getting Started with the Template
----------------------------------

Before you can start using this template for your deep learning and neuroscience projects, you need to set up the environment. Follow the steps below to get started:

1. **Clone the Repository**: First, clone this repository to your local machine using Git:

   .. code-block:: shell

       git clone https://github.com/costantinoai/dnn_template.git
       cd dnn_template

2. **Create a Virtual Environment (Optional)**: It's recommended to create a virtual environment to manage project dependencies. You can use venv or conda for this purpose.

   Using venv:

   .. code-block:: bash

       python -m venv venv
       source venv/bin/activate

   Using conda:

   .. code-block:: bash

       conda create --name dnn_template python=3.8
       conda activate dnn_template

3. **Install Dependencies**: Install the required Python packages. There are two ways to install these dependencies:

   The ``environment.yml`` file is the recommended way to replicate the environment as it ensures that all dependencies, including those that need to be installed from specific Conda channels, are correctly set up.
	   
   To create and activate the environment using the ``environment.yml`` file, run the following commands:
	   
   .. code-block:: bash

       conda env create -f environment.yml
       conda activate dnn_template

   This will create a new Conda environment named ``dnn_template`` and activate it.

   Alternatively, you can use the ``requirements.txt`` file to install Python packages. However, note that this method might not install all dependencies correctly, as some packages are best installed through Conda.

   To install the Python packages from the ``requirements.txt`` file using pip, run:

   .. code-block:: bash

     pip install -r requirements.txt

   For packages that need to be installed via Conda, especially those requiring specific channels (like `pytorch`), refer to the `environment.yml` file for the correct installation commands and channels.

Good Practices for Repository Maintenance
=========================================

To ensure the quality and maintainability of this repository, contributors are encouraged to follow these best practices:

To maintain a high standard of quality and efficiency in this repository, contributors are encouraged to adhere to the following best practices:

1. **Docstring and Documentation Standards**:
   - Ensure every function and class includes a comprehensive docstring following the Sphinx format (see below), including descriptions of parameters, return values, and example usage.
   - Update the project documentation for any code changes by running `./docs/update_docs.sh`. Before running, update the script with the correct Conda path and environment name, which can be obtained using `which conda` and `conda info --envs`.

2. **Project Setup and Structure**:
   - Choose meaningful names and create organized folders for your projects.
   - Initialize a Git repository and synchronize with GitHub for version control.
   - Use virtual environments (venv or conda) for dependency management.

3. **Code Quality and Maintenance**:
   - Follow established coding conventions and style guides to ensure readability and maintainability.
   - Regularly refactor code to reduce complexity.
   - Delete dead or unused code and keep notebooks tidy.
   - Write decoupled, modular code to improve testability and maintainability.
   
Docstring Standards
-------------------

.. important:: Every function and class should include a comprehensive docstring following the Sphinx documentation format. This enhances readability and ease of use.

Here's an extended Sphinx docstring template:

.. code-block:: python

    def example_function(param1, param2):
        """
        A brief description of what the function does.

        :param param1: Description of param1 including expected types and constraints.
        :type param1: type or types
        :param param2: Description of param2.
        :type param2: type
        :returns: Description of the return value, with details of types and structure.
        :rtype: type

        :Example:

        >>> example_function('value1', 2)
        expected_output

        """
        # function implementation
        return something

The docstring should contain:

- A brief description of the function's purpose.
- Detailed descriptions of parameters and return values, including types.
- An example usage section demonstrating how to use the function.

Updating Documentation
----------------------

When modifying the codebase or adding new files, it's crucial to update the documentation accordingly. To automate this process, you can use the `update_docs.sh` script. However, manual steps are also necessary to ensure comprehensive documentation.

1. **Automate Documentation Updates**:
   Run the `update_docs.sh` script located in the `./docs` directory to automatically update the documentation.

   .. code-block:: bash

       ./docs/update_docs.sh

   Before running the script, ensure it points to the correct Conda path and environment:

   - To find your Conda path, use `which conda` in your terminal.
   - Ensure the environment name in the script matches your Conda environment.
   - Update the script with the correct Conda path and environment name:

     .. code-block:: bash

         #!/bin/bash
         # Activate the Conda environment
         source /path/to/conda activate your_env_name
         # Rest of the script

2. **Manually Update Documentation for New Modules**:
   When adding new modules or files, manually update the Sphinx documentation:

   - **Create a New `.rst` File**: For each new module or file, create a new `.rst` file in the `./docs/source` directory. This file should include the module's docstrings and any additional explanatory text.
   
   - **Update the toctree in `index.rst`**:
     Edit the ``index.rst`` file in the ``./docs/source`` directory to include the new rst file in the ``toctree`` directive.

     .. code-block:: rst

         .. toctree::
            :maxdepth: 2
            :caption: Contents:

            module_1
            module_2
            new_module   # Add your new module here

   - **Add Content to the New `.rst` File**:
     The new `.rst` file should follow this basic structure:

     .. code-block:: rst

         New Module
         ===========

         .. automodule:: path.to.new_module
            :members:
            :undoc-members:
            :show-inheritance:

     Replace `path.to.new_module` with the actual import path of your new module.

By following these steps, you can ensure that the documentation remains up-to-date with the latest changes and additions to the codebase.


Usage
=====

You're all set! Start exploring the template by reviewing the project structure and diving into the code.
   
- Check out the `examples/` directory for sample scripts.
- Refer to the documentation for detailed usage instructions.

.. note::
   If you encounter any issues or have suggestions for improvements, please feel free to contribute to this open-source project on GitHub.


