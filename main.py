import time
t = time.time()
import os, re, json, subprocess, numpy as np, nltk
import math, string
from format import *
from nn.grading import framework
from nltk.corpus import stopwords
sw = stopwords.words("english")

p = packet("CO-18-M205-S")#, list(ask("Directory name of a packet: ")))
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
#tokens text
tokens = token(dtext)
OGtokens = sorted(list(set([word for packet in tokens for token in packet for word in token])))
#Word2Vec alg applied and creates vecs
vecs = vectorize(flatten(tokens, 2), show=False, size=100)
#tokens and joins data for Categorizing NN
cdata = [data["challenges"] for data in dadata]
challenges = categorizedData(cdata)
sdata = [data["solutions"] for data in dadata]
solutions = categorizedData(sdata)


print "time:", round(time.time()- t, 3)
