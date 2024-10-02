import random
import pickle
import networkx as nx
from tqdm import tqdm

seed = 42
random.seed(seed)

dataset = '../datasets/collegemsg/collegemsg_raw.txt'

edges = []

with open(dataset, 'r') as file:
    lines = file.readlines()
    for line in lines:
        edge = line.split()
        start, end, timestamp = int(edge[0]), int(edge[1]), eval(edge[2])
        edges.append((start, end, {'timestamp': timestamp}))

# creating a graph from the read edge info
graph = nx.MultiDiGraph()
graph.add_edges_from(edges)

