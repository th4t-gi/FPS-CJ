import time
t = time.time()
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
import subprocess, re

#finds the directory path of given folder
def find_packet(file, rootdir="~/", dir=True):
    if dir:
        d = "d"
    else:
        d = "f"
    try:
        _packet_path = subprocess.check_output("find {} -type {} -name \"{}\"".format(rootdir, d, file),shell=True,stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        _packet_path = e.output
    if not _packet_path.endswith("/"):
        _packet_path = _packet_path.replace('\n', '')
    return _packet_path

def text(key, dictionary, path=False):
    for k, v in dictionary.iteritems():
        if re.match(key, k): yield v
        elif isinstance(v, dict):
            for result in text(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                if type(d) == dict:
                    for result in text(key, d): yield result

def word2vec(l):
    if type(l[0]) == list:
        l = l[0]
    # split each string into words
    l = [string.split(" ") for string in [re.sub(r"[^\w^ ]", "", item).lower() for item in l]]

    # train model
    model = Word2Vec(l, min_count=1)
    # fit a 2d PCA model to the vectors
    X = model[model.wv.vocab]
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    # create a scatter plot of the projection
    pyplot.scatter(result[:, 0], result[:, 1])
    words = [word for word in list(model.wv.vocab) if word]

    formatted = dict(zip(words, X))
    return formatted

# print time.time() - t
