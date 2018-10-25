import time
t = time.time()
import os, re, json, subprocess, numpy as np, nltk
import math, string
from format import *
from keras_attention.lstm import *

p = Getpacket("CO-17-J102-Q")#, list(ask("Directory name of a packet: ")))

#loads found json files and finds all text to be vectorized
dadata = [json.loads(open(i).read()) for i in p.paths]
dtext = [list(getData(r".*?text", data)) for data in dadata]
#add the fuzzy text to become word vectors
for i, ptext in enumerate(dtext):
    ptext.append(open(dadata[i]["meta"]["future-scene"]).read())
#Word2Vec alg applied and creates vecs
tokens = tokenize(dtext)
vecs = vectorize(flatten(tokens, 2), show=False, size=100)
OGtokens = sorted(list(set([word for packet in tokens for token in packet for word in token])))


#challenges data
cdata = [data["challenges"] for data in dadata]
crdata = [data["criteria"] for data in dadata]
challenges = [PairedData(c, vecs) for packet in cdata for c in packet["data"]]

# criteria data

# Procrastinated
# Neural
# Network
# Stuff

print "time:", round(time.time()- t, 3)
