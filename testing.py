import time
t = time.time()

# from keras.layers import LSTM, Bidirectional, Dense, Input
# from keras.utils import plot_model
# from keras.models import Model
# import matplotlib.pyplot as plt, numpy as np, pickle
# from format import get_time
#
# batched = pickle.load(open('batches.p', 'rb'))
# # batched = [tup[1] for tup in batched]
# print batched
# obj = sorted(set(batched))
#
# b = [batched.count(num) for num in obj]
#
# y_pos = np.arange(len(obj))
# plt.bar(y_pos, b)
# plt.xticks(y_pos, obj)
# plt.ylabel('Number of sequences of length')
# plt.title("FPS CJ training data lengths")
#
# plt.show()
# get_time(t).final()


from keras.preprocessing.sequence import pad_sequences
import pickle, numpy as np

y = pickle.load(open('vecs.p', 'rb'))
x = [[.1, .2], [3,4,5], [4], [7,8,9,10]]
x = np.array([np.array(xi) for xi in x])

print pad_sequences(x, padding='post', value=99)
# PURPLE = '\033[95m'
# CYAN = '\033[96m'
# DARKCYAN = '\033[36m'
# BLUE = '\033[94m'
# GREEN = '\033[92m'
# YELLOW = '\033[93m'
# RED = '\033[91m'
# BOLD = '\033[1m'
# UNDERLINE = '\033[4m'
# END = '\033[0m'
