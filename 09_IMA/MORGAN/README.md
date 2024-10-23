# IMA documentation

## Overview

This document explains how to run the IMA component, i.e., MORGAN, and replicate the experiment conducted in RQ2 and RQ3 in the paper.


## Repository structure 
 The repository is structured as follows:
 - Datasets: This folder contains the three datasets used to perform the RQ2 and RQ3 experiment
 - Results: This folder contains the results obtained for all the considered configurations (RQ2 and RQ3)

## Modules Description

1. **main.py**:
   - **Purpose**: It is used to run the parser component and replicate the experiment to replicate RQ2 and RQ3 results 
   - **Functionalities**:
     - Data parsing and preprocessing for training and test datasets.
     - Execution of recommendation functions based on preprocessed data.
     - Performance evaluation across different configurations using cross-validation.
     - Interactive command-line interface for selecting operation modes.

2. **rec_engine.py**:
   - **Purpose**: Contains the core functionalities for generating recommendations using graph kernels.
   - **Functionalities**:
     - Implementation of recommendation algorithms.
     - Evaluation of recommendation outcomes over time.

3. **dataset_utilities.py**:
   - **Purpose**: Provides utility functions for data handling and preprocessing.
   - **Functionalities**:
     - Parsing XES files for data transformation.
     - Data encoding and preprocessing for model consumption.
     - Utility functions for file and directory operations.

4. **config.py**:
     - This defines paths, parameters, and other configuration settings for running the RQ2 and RQ3 experiment

## How to Run

1. Ensure Python 3.7 is installed on your system. We used the same requirements of the MORGAN original paper available [here](https://github.com/MDEGroup/MORGAN)
2. Clone the repository or download the files into a local directory.
3. Navigate to the project directory in your terminal or command prompt.
4. Run the following command to start the application:
   ```bash
   python main.py
      ```   
5. Follow the on-screen prompts to select the desired operation mode. In particular: 

      -  type 1: run the trace parser to convert XES models to MORGAN format
      -  type 2: it executes the RQ2 experiment
      -  type 3: it executes the RQ3 experiment
  
**Note that** you may want to configure the training and output local paths in the ```config.py```  file. 