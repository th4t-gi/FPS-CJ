import time
t = time.time()
# import keras.backend as K
# from keras.layers import LSTM, Bidirectional, Dense, Input
# from keras.utils import plot_model
# from keras.models import Model
# import matplotlib
from format import get_time, flatten

input = Input(shape=(None, 100))
lstm_out = Bidirectional(LSTM(32, return_sequences=True))(input)
output = Dense(22, activation='softmax')(lstm_out)

model = Model(inputs=input, outputs=output)
model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])
plot_model(model, to_file='categorizing_model.png')


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
