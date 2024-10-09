import pickle
from gensim.models import Word2Vec

temporal_walks_file = '../datasets/collegemsg/temporal_walks.pkl'

# loading temporal walks
with open(temporal_walks_file, 'rb') as file:
    temporal_walks = pickle.load(file)

# word2vec model configs
embed_dim = 512
window = 10
min_count = 1
workers = 4

# actual word2vec model training
w2v = Word2Vec(sentences = temporal_walks, 
              vector_size = embed_dim, 
              window = window, 
              min_count = min_count, 
              workers = workers)

