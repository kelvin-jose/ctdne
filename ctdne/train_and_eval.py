import pickle

temporal_walks_file = '../datasets/collegemsg/temporal_walks.pkl'

# loading temporal walks
with open(temporal_walks_file, 'rb') as file:
    temporal_walks = pickle.load(file)