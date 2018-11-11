from keras.layers import LSTM, Bidirectional, Dense, Input, Flatten
from keras.utils import plot_model
from keras.models import Model, load_model, save_model#, load_weights, save_weights
from keras_proxy.models.custom_recurrents import AttentionDecoder

from format import flatten


# class base_model(object):
#
#     def __init__(self):
#         super(base_model, self).__init__()
def get_context_vector(features=100, units=None, *metrics):
    metrics = flatten([list(metrics), "accuracy"])

    input = Input(shape=(units, features))
    lstm_out = Bidirectional(LSTM(50, return_sequences=True))(input)
    attended = AttentionDecoder(features, 1, name="Attention")(lstm_out)
    return Flatten()(attended)

def plain_coder(featues=100, *metrics):

    # Define an input sequence and process it.
    encoder_inputs = Input(shape=(None, features))
    encoder = LSTM(latent_dim, return_state=True)
    encoder_outputs, state_h, state_c = encoder(encoder_inputs)
    # We discard `encoder_outputs` and only keep the states.
    encoder_states = [state_h, state_c]

    # Set up the decoder, using `encoder_states` as initial state.
    decoder_inputs = Input(shape=(None, features))
    # We set up our decoder to return full output sequences,
    # and to return internal states as well. We don't use the
    # return states in the training model, but we will use them in inference.
    decoder = LSTM(latent_dim, return_sequences=True, return_state=True)
    decoder_outputs, _, _ = decoder(decoder_inputs, initial_state=encoder_states)
    decoder_outputs = Dense(num_decoder_tokens, activation='softmax')(decoder_outputs)

    model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
    model.compile(optimizer='rmsprop', loss='categorical_crossentropy')
    model.fit([encoder_input_data, decoder_input_data], decoder_target_data)


def Categorizing_model(features=100, units=None, *metrics):
    # metrics = flatten([list(things), "accuracy"])
    #
    # input = Input(shape=(None, features))
    # lstm_out = Bidirectional(LSTM(50, return_sequences=True))(input)
    # attended = AttentionDecoder(1, features, name="Attention")(lstm_out)
    # context_vector = Flatten()(attended)
    context_vector = get_context_vector(features, units, metrics)
    output = Dense(22, activation='softmax')(context_vector)

    model = Model(inputs=input, outputs=output)
    model.compile(loss='categorical_crossentropy', optimizer='adadelta', metrics=metrics)

    return model

def relevent_model(features=100, *metrics):
    # metrics = flatten([list(things), "accuracy"])
    #
    # input = Input(shape=(None, features))
    # lstm_out = Bidirectional(LSTM(50, return_sequences=True))(input)
    # attended = AttentionDecoder(1, features, name="Attention")(lstm_out)
    context_vector = get_context_vector(features, metrics)
    output = Dense(1, kernel_initializer='normal', activation='sigmoid')(context_vector)

    model = Model(inputs=input, outputs=output)
    model.compile(loss='binary_crossentropy', optimizer='adadelta', metrics=metrics)

    # I think this is it...
    return model

def clarity_model(features=100, *metrics):

    context_vector = get_context_vector(features, metrics)

    # something with plain_coder()
