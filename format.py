from time import time
t = time()
from nltk.tokenize import word_tokenize
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
from collections import namedtuple, OrderedDict
from platform import mac_ver
import subprocess, re, os, numpy as np, random, string, warnings, pickle

#finds the directory path of given folder
def find_dir(file, rootdir="~/", dir=True):
    if dir: d = "d"
    else: d = "f"
    try:
        _packet_path = subprocess.check_output("find {} -type {} -name \"{}\"".format(rootdir, d, file),shell=True,stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        _packet_path = e.output
    if not _packet_path.endswith("/"):
        _packet_path = _packet_path.replace('\n', '')
    return _packet_path

class Getpacket(object):

    def __init__(self, *args):
        super(Getpacket, self).__init__()
        self.packets = flatten(args)
        self.packets = list(set(flatten([self.get_packets(i) for i in self.packets])))
        self.paths = [self.get_data(i) for i in self.packets]
        self.paths = [j for i in self.paths for j in i if not j == "NO PACKET"]
        if not self.paths:
            self.isdata("packets")


    def get_data(self, packet):
        if not packet:
            return ["NO PACKET"]
        self.packet = packet.upper()
        requested_packet = not(self.packet == "ALL")
        flashdrive = "no" #raw_input("Is the packet {} on a USB drive?(yes/no): ".format(packet))

        if flashdrive == "yes":
            flashdrive = raw_input("What is the name of the USB drive?: ")
            if flashdrive.lower() in [item.lower() for item in os.listdir("/Volumes")]:
                os.chdir("/Volumes/{}".format(flashdrive))
                paths = find_dir(self.packet, os.getcwd())
        #finds path to given packet, or all packets
        try:
            self.data = find_dir(self.packet, os.getcwd().replace(" ", "\ "))
            if not self.isdata():
                return ["NO PACKET"]
            self.data = ''.join(re.split(re.compile(r"({})".format(self.packet)), self.data)[:2]) + "/"
            self.data = [self.data + i for i in os.listdir(self.data) if 'data' in i]
            print "\033[1mFound Packet:\033[0m", self.packet
        except subprocess.CalledProcessError as e:
            self.data = e.output
        except OSError:
            print self.packet
            print "invalid packet directory: {}".format(self.packet)
            quit()
        return self.data

    def get_packets(self, packet):
        if packet == "ALL":
            paths = subprocess.check_output("find -E . -regex '.*/data-[0-9]{3}\.json' -type f",shell=True,stderr=subprocess.STDOUT)
            paths = [i for i in paths.split("\n") if i and os.path.basename(os.path.dirname(i)) not in self.packets]
            packet = [os.path.basename(os.path.dirname(i)) for i in paths]
        return packet

    def isdata(self, check=None):
        if check == "packets":
            tp = find_dir("Training packets", rootdir=os.getcwd().replace(" ", "\ "))
            if not tp:
                yn = raw_input("No training packets detected, would you like to download? (y/n): ")
                if yn == "y":
                    dump_data()
            return True
        if not self.data:
            print "\033[91m{}\033[0m is not a packet".format(str(self.packet))
            quit()
        return True


class CatorableSample(object):

    GP = ["categories", "perhaps", "why", "duplicate", "solution"]
    CP = {GP[1]: 19, GP[2]: 20, GP[3]: 21, GP[4]: 22}

    def __init__(self, data):
        super(CatorableSample, self).__init__()
        vecs = pickle.load(open("vecs.p", "rb"))
        # finds text from data obj
        self.type = find_type(data)
        self.tokens = tokenize(data["packet"]["text"], single=True)
        self.words = data["packet"]["text"]
        #finds categories for the self.tokens
        self.category = [tup for tup in data["scoring"].items() if tup[0] in self.GP]
        self.category = [tup for tup in self.category if tup[1]][0]
        if self.category[0] == "categories":
            self.category = self.category[1]
        self.c = self.category
        if not(type(self.category) in (int, list)):
            self.category = self.CP[self.category[0]]
        self.category = self.onehot(self.category)
        #combines self.tokens and self.categorys
        self.vecs = np.array([vecs[token] for token in self.tokens])
        self.v = OrderedDict(zip(self.tokens, self.vecs))
        if self.type == "challenge":
            self.yes = self.onehot(data["scoring"]["yes"])
        else:
            self.yes = self.onehot(data["scoring"]["relevant"])



    def onehot(self, data):
        if type(data) == bool:
            return int(data)
        else:
            cat = [0 for _ in range(22)]
            if type(data) == list:
                cat[data[0]] = 1
                cat[data[1]] = 1
            else:
                cat[data] = 1
            return cat


class get_time(object):

    def __init__(self, t=None):
        super(get_time, self).__init__()
        self.time = time()
        if t:
            self.time = t

    def final(self):
        print "time:", round(time()- self.time, 3)


def dump_data():
    path = os.getcwd() + "/Training packets"
    pathyn = raw_input("(y/n) save training packets in {}?: ".format(path))

    if pathyn == "y":
        cmd = "svn checkout https://github.com/th4t-gi/FPS-CJ/trunk/Training%20packets {} --force -q".format(path.replace(" ", "\ "))
        os.system(cmd)

def dump_vectors(vecs):
    if False
        if not os.path.isfile("vecs.p"):
            pickle.dump(vecs, open("vecs.p", "wb"))

        v = pickle.load(open("vecs.p", "rb"))
        try:
            np.testing.assert_equal(vecs, v)
        except AssertionError:
            pickle.dump(vecs, open("vecs.p", "wb"))

def get_values(key, dictionary, track=False):
    for k, v in dictionary.iteritems():
        if re.match(key, k): yield v
        elif isinstance(v, dict):
            for result in get_values(key, v):
                yield result
        elif isinstance(v, list):
            for i, d in enumerate(v):
                if track:
                    yield i
                if type(d) == dict:
                    for result in get_values(key, d): yield result

def vectorize(l, show=False, size=100, sim=[]):
    warnings.simplefilter(action="ignore", category=FutureWarning)
    # train model
    model = Word2Vec(l, min_count=1, size=size)
    X = model[model.wv.vocab]
    words = [word for word in list(model.wv.vocab) if word]
    formatted = dict(zip(words, X))
    if sim and len(sim) in [2, 3]:
        if len(sim) == 2:
            result = model.most_similar(positive=[sim[0]], negative=[sim[1]], topn=5)
        else:
            result = model.most_similar(positive=[sim[0], sim[2]], negative=[sim[1]], topn=5)
        print result
    if show:
        # create a scatter plot of the projection
        pca = PCA(n_components=2)
        result = pca.fit_transform(X)
        pyplot.scatter(result[:, 0], result[:, 1])
        words = list(model.wv.vocab)
        for i, word in enumerate(words):
        	pyplot.annotate(word, xy=(result[i, 0], result[i, 1]))
        pyplot.show()

    return formatted


def tokenize(text, single=False):
    if single:
        tokens = word_tokenize(text.replace("/", " ").replace("\"", ""))
        return [word.lower() for word in tokens if not word.lower() in string.punctuation if not "'" in word]
    if not type(text[0]) == list:
        raise TypeError("Text must be nested list of strings, not list of type str")
    tokens = [[word_tokenize(i.replace("/", " ").replace("\"", "")) for i in packet] for packet in text]
    return [[[word.lower() for word in i if not word.lower() in string.punctuation if not "'" in word] for i in packet] for packet in tokens]

def flatten(l, iter=float("inf")):
    result = []
    for el in l:
        if iter == 0:
            result.append(l)
            break
        if isinstance(el, dict):
            result.append(el)
        elif hasattr(el, "__iter__") and not isinstance(el, basestring):
            result.extend(flatten(el, iter - 1))
        else: result.append(el)
    return result

def ask(ask):
    while True:
        result = raw_input(ask)
        if result == "" or result == "ALL" or result.endswith(";"):
            yield result.replace(";", ""); break
        else: yield result; continue

def get_version():
    return float('.'.join(mac_ver()[0].split(".")[:2]))

def find_type(data):
    try:
        something = data["scoring"]["solution"]
        return "challenge"
    except:
        return "solution"
# get_time(t).final()
