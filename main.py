import time
t = time.time()
import os, re, json, subprocess, numpy as np, nltk
import math, string
from format import *
from models import *

if get_version() > 10.11:
    from keras_attention.lstm import *

p = Getpacket("CO-18-M205-S")

#loads found json files and finds all text to be vectorized
dadata = [json.loads(open(i).read()) for i in p.paths]
dtext = [list(get_values(r".*?text", data)) for data in dadata]
#add the fuzzy text to become word vectors
for i, ptext in enumerate(dtext):
    ptext.append(open(dadata[i]["meta"]["future-scene"]).read())
#Word2Vec alg applied and creates vecs
tokens = tokenize(dtext)
vecs = vectorize(flatten(tokens, 2), show=False, size=100)
OGtokens = sorted(set(flatten(tokens)))

#challenges data
cdata = [[data["challenges"], data["solutions"]] for data in dadata]
crdata = [data["criteria"] for data in dadata]
# challenges = [PairedData(c, vecs) for packet in cdata for c in packet["data"]]
# cats = PairedData(cdata, vecs)``
ddata = flatten([i["data"] for i in flatten(cdata)])
cats = PairData(ddata, vecs, sorted=True)
cmodel = Categorizing_model()
cmodel.fit(cats[0][0], cats[1][0])#, batch_size=len(cats[0]))
# for c in challenges:
#     print c.words
#     print c.vecs
#     print c.category
#     print c.c
#     print "\n"

# criteria data

# Procrastinated
# Neural
# Network
# Stuff

get_time(t).final()
