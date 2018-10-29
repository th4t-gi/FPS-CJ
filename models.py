from keras.layers import LSTM, Bidirectional, Dense, Input, Flatten
from keras.utils import plot_model
from keras.models import Model


def Categorizing_model():
    input = Input(shape=(None, 100))
    lstm_out = Bidirectional(LSTM(10, return_sequences=True))(input)
    something = Flatten()(lstm_out)
    output = Dense(22, activation='softmax')(something)

    model = Model(inputs=input, outputs=output)
    model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=['accuracy'])

    #And then someway to do Attention

    return model
