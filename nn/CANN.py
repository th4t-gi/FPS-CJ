import numpy as np
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
import pickle
np.random.seed(1)


class _neuralnet(object):

    def __init__(self, input, layers):
        if type(layers) != list:
            self._type = type(layers).__name__
            raise TypeError("layers parameter needs to be type list not type {0}".format(self._type))

        self.out = layers[-1]
        self.hidden = layers[:-1]

    def nonlinear(self, x, deriv=False):
        if deriv:
            return x*(1 - x)
        return 1 / (1 + np.exp(-x))

    def cost(self, guessed):
        return (guessed - self.result)*(guessed - self.result)

    def train(self, iter):
        pass

class CataNN(_neuralnet):

    def __init__(self, struct, core, data):
        """A child neural network class for classifying the problems and solutions
        in a FPS packet"""

        if not((isinstance(struct, list) and len(struct) == 2) or isinstance(core, str) or isinstance(data, list)):
            raise NameError("CataNN.__init__ arguments are of incorrect format")

        core = word_tokenize(core)
        self.o = [word for word in [core[(i + 1):] for i, el in enumerate(core) if el == ')'][0]
                if word.lower() not in stopwords.words('english') and len(word) > 1]
        self.o = self.w2v(self.o)

        super(CataNN, self).__init__(self.o, struct)

    def w2v(self, words):
        return words
