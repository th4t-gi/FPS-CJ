from keras.layers import LSTM, Bidirectional, Dense, Input, Flatten
from keras.utils import plot_model
from keras.models import Model
from attention_decoder import AttentionDecoder


# class base_model(object):
#
#     def __init__(self):
#         super(base_model, self).__init__()
def Categorizing_model(*metrics, features=100):
    metrics = flatten([list(things), "accuracy"])

    input = Input(shape=(None, features))
    lstm_out = Bidirectional(LSTM(50, return_sequences=True))(input)
    attended = AttentionDecoder(1, features, name="Attention")(lstm_out)
    context_vector = Flatten()(attended)
    output = Dense(22, activation='softmax')(context_vector)

    model = Model(inputs=input, outputs=output)
    model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=metrics)

    return model

def relevent_model(*metrics, features=100):
    metrics = flatten([list(things), "accuracy"])

    input = Input(shape=(None, features))
    lstm_out = Bidirectional(LSTM(50, return_sequences=True))(input)
    attended = AttentionDecoder(1, features, name="Attention")(lstm_out)
    output = Dense(1, kernel_initializer='normal', activation='sigmoid')(attended)

    model = Model(inputs=input, outputs=output)
    model.compile(loss='binary_crossentropy', optimizer='adadelta', metrics=metrics)

    # I think this is it...
    return model

def 
