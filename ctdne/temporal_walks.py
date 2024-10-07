import random
import pickle
import networkx as nx

seed = 42
random.seed(seed)

train_edges_file = '../datasets/collegemsg/train_edges.pkl'

with open(train_edges_file, 'rb') as te:
    train_edges = pickle.load(te)

