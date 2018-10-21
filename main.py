import time
t = time.time()
import os, re, json, subprocess, numpy as np, nltk
import math, string
from format import *

p = Getpacket("ALL")#, list(ask("Directory name of a packet: ")))
#write the filepath to data
for i, val in enumerate(p.paths):
    fuzzy = find_packet("fuzzy.txt", re.sub(r"data-\d{3}\.json", "", p.paths[i]).replace(" ", "\\ "), dir=False)
    jeff = open(p.paths[i]).read()
    with open(val, "r+") as f:
        f.write(re.sub(r"future-scene\": \".*?\"", "future-scene\": \"{}\"".format(fuzzy),
                re.sub(r"data-filepath\": \".*?\"", "data-filepath\": \"{}\"".format(val), jeff)))

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
