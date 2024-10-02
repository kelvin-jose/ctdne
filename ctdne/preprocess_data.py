import random
import pickle
import networkx as nx
from tqdm import tqdm
from typing import List, Tuple

seed = 42
random.seed(seed)

dataset = '../datasets/collegemsg/collegemsg_raw.txt'
train_percent = 0.75

# reading a dataset file and returns edge list
def get_edgelist(filename: str) -> list:
    edges = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            edge = line.split()
            start, end, timestamp = int(edge[0]), int(edge[1]), eval(edge[2])
            edges.append((start, end, {'timestamp': timestamp}))
    return edges

# given a graph, get train and test edges
def get_train_test_data(graph: nx.Graph) -> Tuple[List, List, List]:
    train_edges = []
    pos_edges = []
    neg_edges = []

    # train and test data split 
    for node in tqdm(graph.nodes):
        out_edges = graph.edges(node, data=True)
        if not out_edges:
            continue
        out_edges = sorted(out_edges, key=lambda x: x[2]['timestamp']) # sorting data in the ascending order of edge times
        last_train_idx = int(len(out_edges) * train_percent) # 75% of data is used for training
        train_edges.extend(out_edges[:last_train_idx])
        pos_edges.extend(out_edges[last_train_idx:]) # 25% data is used for testing (positive examples)

        neighbors = set(graph.neighbors(node))
        non_neighbors = set(graph.nodes).difference(neighbors)
        neg_nodes = random.sample(sorted(non_neighbors), len(out_edges[last_train_idx:])) # generating same 25% negative data for testing
        neg_edges.extend([(node, nnode)for nnode in neg_nodes])

    return train_edges, pos_edges, neg_edges

# save data to disk
def pickle_data(data: List, filename: str) -> None:
    with open(filename, 'wb') as file:
        pickle.dump(data, file)
    print(f'[x] pickled data dumped to: {filename}')


if __name__ == '__main__':

    edges = get_edgelist(dataset)

    # creating a graph from the read edge info
    graph = nx.MultiDiGraph()
    graph.add_edges_from(edges)

    train_edges, pos_edges, neg_edges = get_train_test_data(graph)

    # writing train - test data to disk
    pickle_data('../datasets/collegemsg/train_edges.pkl', train_edges)
    pickle_data('../datasets/collegemsg/positive_edges.pkl', pos_edges)
    pickle_data('../datasets/collegemsg/negative_edges.pkl', neg_edges)
