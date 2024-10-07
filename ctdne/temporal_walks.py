import random
import pickle
import networkx as nx

seed = 42
random.seed(seed)

train_edges_file = '../datasets/collegemsg/train_edges.pkl'

# loading edge info
with open(train_edges_file, 'rb') as te:
    train_edges = pickle.load(te)

# graph from edge info
graph = nx.MultiDiGraph()
graph.add_edges_from(train_edges)

N = len(graph.nodes)
omega = 10 # context window size
L = 80 # max length of walk
beta = 25 * N * (L - omega + 1)