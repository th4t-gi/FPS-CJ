import time
t = time.time()
# import keras.backend as K
from keras.layers import LSTM, Bidirectional, Dense, Input
from keras.utils import plot_model
from keras.models import Model
import matplotlib
from keras_attention.lstm import *

input = Input(shape=(None, 100))
lstm_out = Bidirectonal(LSTM(32, return_sequences=True)(input))
output = Dense(22, activation='softmax')(lstm_out)

model = Model(inputs=inputs, outputs=output)
model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])
print model.summary()
some_data = None
some_labes = None
model.fit(some_data, some_labels, epochs=100)
# model_attention_applied_after_lstm()

get_time(t).final()

# PURPLE = '\033[95m'
# CYAN = '\033[96m'
# DARKCYAN = '\033[36m'
# BLUE = '\033[94m'
# GREEN = '\033[92m'
# YELLOW = '\033[93m'
# RED = ''
# BOLD = '\033[1m'
# UNDERLINE = '\033[4m'
# END = '\033[0m'
