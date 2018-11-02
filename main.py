import time
t = time.time()
import os, re, json, subprocess, pickle, numpy as np, nltk
import math, string
from format import *
if get_version() > 10.11:
    from models import *

# LOAD DATA
p = Getpacket("ALL")

#loads found json files and finds all text to be vectorized
dadata = [json.loads(open(i).read()) for i in p.paths]
dtext = [list(get_values(r".*?text", data)) for data in dadata]
#add the fuzzy text to become word vectors
for i, ptext in enumerate(dtext):
    ptext.append(open(os.getcwd() + dadata[i]["meta"]["future-scene"]).read())

#Word2Vec alg applied and creates vecs
tokens = tokenize(dtext)
vecs = vectorize(flatten(tokens, 2), show=False, size=100)
dump_vectors(vecs)

OGtokens = sorted(set(flatten(tokens)))

#challenges data
cdata = [[data["challenges"], data["solutions"]] for data in dadata]

temp_data = flatten([i["data"] for i in flatten(cdata)])
cats = [[CatorableSample(c).vecs for c in temp_data], [CatorableSample(c).category for c in temp_data]]
# APPLY MODELS
categorable = Categorizing_model()
# categorable.fit(cats[0], cats[1])
#
# yes = [[CatorableSample(c).vecs for c in temp_data], [CatorableSample(c).yes for c in temp_data]]
# rel_model = relevent_model()
# rel_model.fit(yes[0], yes[1])


# for i in cdata[0]:
#     for c in i["data"]:
#         CatorableSample(c)

crdata = [data["criteria"] for data in dadata]

# criteria data

# Procrastinated
# Neural
# Network
# Stuff

get_time(t).final()
