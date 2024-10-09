# Continuous-Time Dynamic Network Embeddings (CTDNE)

This repository contains the code for the CTDNE method, as described in the paper [Continuous-Time Dynamic Network Embeddings](https://dl.acm.org/doi/fullHtml/10.1145/3184558.3191526). The code implements a framework for generating dynamic network embeddings using temporal walks and evaluates the embeddings with a logistic regression classifier.

## Table of Contents
- [Abstract](#abstract)
- [Installation](#installation)
- [Usage](#usage)
- [File Descriptions](#file-descriptions)
- [Results](#results)
- [References](#references)
- [License](#license)

## Abstract
This codebase provides tools for preprocessing temporal network data, generating temporal walks, and training embeddings. It includes implementations for data splitting, embedding training using Word2Vec, and model evaluation using logistic regression.

## Installation
To run this code, you will need Python 3.x and the following packages:

```bash
pip install networkx tqdm gensim scikit-learn