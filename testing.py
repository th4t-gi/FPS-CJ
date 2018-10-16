import time
t = time.time()
import tensorflow as tf
import keras
from keras.layers import LSTM, Bidirectional, Dense, Input, Embedding
from keras.utils import plot_model
from keras.models import Model
import matplotlib

main_input = Input(shape=(100,), name="main_input")
# x = Embedding(output_dim=512, input_dim=10000, input_length=100)(main_input)
#
# class color:
#     PURPLE = '\033[95m'
#     CYAN = '\033[96m'
#     DARKCYAN = '\033[36m'
#     BLUE = '\033[94m'
#     GREEN = '\033[92m'
#     YELLOW = '\033[93m'
#     RED = ''
#     BOLD = '\033[1m'
#     UNDERLINE = '\033[4m'
#     END = '\033[0m'
#
# print color.BOLD + 'Hello World !' + color.END
# print color.RED + 'Hello World !' + color.END
# print color.DARKCYAN + 'Hello World !' + color.END
# print color.PURPLE + 'Hello World !' + color.END
# print color.BLUE + 'Hello World !' + color.END
