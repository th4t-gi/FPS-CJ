import time
t = time.time()
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from matplotlib import pyplot
import subprocess, re, os

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

def get_packet():
    packet = raw_input("folder name of packet: ").upper()
    flashdrive = "no" #raw_input("Is the file on a USB drive?(yes/no): ")

    if flashdrive == "yes":
        flashdrive = raw_input("What is the name of the USB drive?: ")
        if flashdrive.lower() in [item.lower() for item in os.listdir("/Volumes")]:
            os.chdir("/Volumes/{}".format(flashdrive))
            paths = find_packet(packet, os.getcwd())
    elif packet:
        print "OK"
        paths = find_packet(packet, "~/Code/")
        paths = ''.join(re.split(re.compile(r"({})".format(packet)), paths)[:2]) + "/"
    #finds path to given packet, or all packets
    try:
        if not packet:
            print "OK"
            paths = subprocess.check_output("find ~/Code/ -regex \".*/data-[^score].*\.json\" -type f",shell=True,stderr=subprocess.STDOUT)
            paths = [i for i in paths.split("\n") if i]
        else:
            paths = [paths + i for i in os.listdir(paths) if 'data' in i]
    except OSError:
        print "invalid packet directory: {}".format(packet)
        quit()
    except IndexError:
        print "packet file(s) not found"
    except subprocess.CalledProcessError as e:
        paths = e.output

    return [packet, paths]


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

def word2vec(l, packet=True):
    # split each string into words
    if not packet:
        l = [re.sub(r"[^\w^ ]", "", re.sub(r"/", " ", string)).lower().split(" ") for packet in l for string in packet]
    else:
        l = [re.sub(r"[^\w^ ]", "", string).lower().split(" ") for string in l[0]]
    # train model
    model = Word2Vec(l, min_count=1)
    # fit a 2d PCA model to the vectors
    X = model[model.wv.vocab]
    pca = PCA(n_components=2)
    result = pca.fit_transform(X)
    words = [word for word in list(model.wv.vocab) if word]
    formatted = dict(zip(words, X))
    return formatted

# print time.time() - t
