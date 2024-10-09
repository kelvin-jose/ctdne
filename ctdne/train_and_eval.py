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

# loading data for evalution
pos_edges_file = '../datasets/collegemsg/positive_edges.pkl'
neg_edges_file = '../datasets/collegemsg/negative_edges.pkl'

with open(pos_edges_file, 'rb') as pfile, open(neg_edges_file, 'rb') as nfile:
    pos_edges = pickle.load(pfile)
    neg_edges = pickle.load(nfile)

# data prep for evaluation
eval_dataX = []
eval_datay = []
keys = w2v.wv.key_to_index.keys()

for positive, negative in list(zip(pos_edges, neg_edges)):
    if positive[0] in keys and negative[0] in keys and positive[1] in keys and negative[1] in keys:
        eval_dataX.append((w2v.wv.get_vector(positive[0]) + w2v.wv.get_vector(positive[1]))/2)
        eval_dataX.append((w2v.wv.get_vector(negative[0]) + w2v.wv.get_vector(negative[1]))/2)
        eval_datay.extend([1,0])

