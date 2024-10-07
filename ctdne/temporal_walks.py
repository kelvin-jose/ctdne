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

C = 0
temporal_walks = []
edges = list(graph.edges(data=True))

while beta - C > 0:
    walk = []
    first_edge = random.sample(edges, k=1) # unbiased first edge 
    u, v = first_edge[0][:2]
    walk.append(u)
    walk.append(v)
    vtime = first_edge[0][2]['timestamp']
    
    for i in range(L - 2):
        vneighbors = list(graph.out_edges(v, data=True))
        temp_neighbors = list(filter(lambda x: x[2]['timestamp'] >= vtime, vneighbors))
        if temp_neighbors:
            next_edge = random.sample(temp_neighbors, k=1)[0]
            v, vtime = next_edge[1], next_edge[2]['timestamp']
            walk.append(v)
            
    if len(walk) >= omega:
        temporal_walks.append(walk)
        C += len(walk) - omega + 1