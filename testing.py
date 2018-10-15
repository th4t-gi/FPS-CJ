# # import time
# # t = time.time()
# # import tensorflow as tf
# # import keras
# # from keras.layers import LSTM, Bidirectional, Dense, Input
# # from keras.utils import plot_model
# # from keras.models import Model
# # import matplotlib
# #
# # visible = Input(shape=(100,1))
# # model = LSTM(25, return_sequences=True)(visible)
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
def flatten(l, iter=float("inf")):
    result = []
    for el in l:
        if iter == 0:
            result.append(l)
            break
        if hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el, iter - 1))
        else: result.append(el)
    return result

a = ["I", "am", ["fine", "good", "bad"], ["ok", "OKAY", ["okay"]]]
print flatten(a)
print flatten(a, 1)
