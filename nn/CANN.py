import numpy as np, pickle, re
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords
np.random.seed(1)

class _neuralnet(object):

    def __init__(self, l0, layers):
        if type(layers) != list:
            self._type = type(layers).__name__
            raise TypeError("layers parameter needs to be type list not type {0}".format(self._type))

        self.out = layers[-1]
        self.hidden = layers[:-1]
        self.weights = []

        if self.hidden:
            self.hidden.insert(0, l0)
            for i in range(1, len(self.hidden)):
                self.weights.append(np.random.random((self.hidden[i], self.hidden[i - 1])))
        else:
            weights = np.random.random((self.out, len(l0) - 1))

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

        contrxs = {"aren't" : "are not", "can't" : "cannot", "couldn't" : "could not", "didn't" : "did not", "doesn't" : "does not", "don't" : "do not", "hadn't" : "had not", "hasn't" : "has not", "haven't" : "have not", "he'd" : "he had", "he'll" : "he will", "he's" : "he is; he has",
                "I'd" : "I had", "I'll" : "I will", "I'm" : "I am", "I've" : "I have", "isn't" : "is not", "let's" : "let us", "mightn't" : "might not", "mustn't" : "must not", "shan't" : "shall not", "she'd" : "she had", "she'll" : "she will", "she's" : "she is", "shouldn't" : "should not",
                "that's" : "that is", "there's" : "there is", "they'd" : "they had", "they'll" : "they will", "they're" : "they are", "they've" : "they have", "we'd" : "we had", "we're" : "we are", "we've" : "we have", "weren't" : "were not", "what'll" : "what will", "what're" : "what are",
                "what's" : "what is", "what've" : "what have", "where's" : "where is", "who's" : "who had", "who'll" : "who will", "who're" : "who are", "who's" : "who is", "who've" : "who have", "won't" : "will not", "wouldn't" : "would not", "you'd" : "you had", "you'll" : "you will", "you're" : "you are", "you've" : "you have"}

        self.data = data
        core = ' '.join([contrxs[word] if word in contrxs.keys() else word for word in core.split()])
        core = word_tokenize(re.sub(r" \(not sure\)", '', core))
        self.o = [word for word in [core[(i + 1):] for i, el in enumerate(core) if el == ')'][0]
                if word.lower() not in stopwords.words('english') and re.search(r"(\w+)", word) and not "'" in word]
        self.w2v()

        super(CataNN, self).__init__(self.o, struct)

    def w2v(self):
        # print self.o
        pass
