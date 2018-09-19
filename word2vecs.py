from gensim.models.keyedvectors import KeyedVectors

model = KeyedVectors.load_word2vec_format('path/to/GoogleNews-vectors-negative300.bin', binary=True)
model.save_word2vec_format('path/to/GoogleNews-vectors-negative300.txt', binary=False)
