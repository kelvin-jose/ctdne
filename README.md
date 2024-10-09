# Continuous-Time Dynamic Network Embeddings (CTDNE)

This repository contains the code for the CTDNE method, as described in the paper [Continuous-Time Dynamic Network Embeddings](https://dl.acm.org/doi/fullHtml/10.1145/3184558.3191526). The code implements a framework for generating dynamic network embeddings using temporal walks and evaluates the embeddings with a logistic regression classifier.


If you are interested to do a deep dive into the paper, I have this [blog post](https://medium.com/@kelvinjose/continuous-time-dynamic-network-embeddings-4d3dd0ac9aaa) ready for you.

## Table of Contents
- [Abstract](#abstract)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Results](#results)
- [References](#references)

## Abstract
This codebase provides tools for preprocessing temporal network data, generating temporal walks, and training embeddings. It includes implementations for data splitting, embedding training using Word2Vec, and model evaluation using logistic regression.

## Installation
To run this code, you will need Python 3.x and the following packages:

```bash
pip install networkx tqdm gensim scikit-learn
```
## Usage
1. Preprocess Data: Run preprocess_data.py to load your dataset and split it into training, positive, and negative edges.

```bash
python preprocess_data.py
```

2. Generate Temporal Walks: Execute temporal_walks.py to create temporal walks from the training edges.
```bash
python temporal_walks.py
```

3. Train and Evaluate the Model: Finally, run train_and_eval.py to train a logistic regression model and evaluate its performance.

```bash
python train_and_eval.py
```

## File Descriptions
1. ```preprocess_data.py```:
    - Reads a raw dataset file and converts it into an edge list.
    - Splits the graph edges into training, positive testing, and negative testing datasets.
    - Saves the processed data to disk using pickle.

2. ```temporal_walks.py```:
    - Loads training edges and constructs a graph.
    - Generates temporal walks based on the edges and timestamps, adhering to a specified context window size and maximum walk length.
    - Saves the generated walks to disk.

3. ```train_and_eval.py```:
    - Loads temporal walks and trains a Word2Vec model to create embeddings.
    - Loads positive and negative edge datasets for evaluation.
    - Prepares evaluation data and trains a logistic regression model.
    - Outputs the accuracy of the model.

## Results
The accuracy of the logistic regression model trained on the embeddings will be printed to the console upon execution of ```train_and_eval.py```.

## References
1. [Continuous-Time Dynamic Network Embeddings](https://dl.acm.org/doi/fullHtml/10.1145/3184558.3191526)