import time
t = time.time()
import tensorflow as tf
import keras
from keras.layers import LSTM, Bidirectional, Dense, Input
from keras.utils import plot_model
from keras.models import Model
import matplotlib

model = LSTM(25, return_sequences=True)
