import time
t = time.time()
import os, re, json, subprocess, pickle, numpy as np, nltk
import math, string
from format import *
from sys import argv
from models import *

# LOAD DATA
p = Getpacket("CO-17-J102-Q")
root = p.root.replace("\ ", " ")
#loads found json files and finds all text to be vectorized

dadata = [json.loads(open(i).read()) for i in p.paths]
dtext = [list(get_values(r".*?text", data)) for data in dadata]
#add the fuzzy text to become word vectors
for i, ptext in enumerate(dtext):
    ptext.append(open(root + dadata[i]["meta"]["future-scene"]).read())

#Word2Vec alg applied and creates vecs
tokens = tokenize(dtext)
vecs = vectorize(flat(tokens, 2), show=False, size=100)
dump_vectors(vecs, os.getcwd())

OGtokens = sorted(set(flat(tokens)))

#challenges data
cdata = [[data["challenges"], data["solutions"]] for data in dadata]

temp_data = flat([i["data"] for i in flat(cdata)])

x, y = [], []
training_cent = int(math.ceil(len(temp_data) * 0.95))
for i, c in enumerate(temp_data):
    s = CatorableSample(c, vecs)
    x.append(np.reshape(s.vecs, (1, ) + s.vecs.shape))
    y.append(np.reshape(s.c, (1, 22)))

batched = sorted([i.shape for i in x])

pickle.dump(batched, open('batches.p', 'wb'))

if 'train' in argv:
    # APPLY MODELS
    categorable = Categorizing_model()

    for i, input in enumerate(x[:training_cent]):
        categorable.fit(input, y[i], epochs=50, verbose=2)
    for i, input in enumerate(x[training_cent:]):
        categorable.evaluate(input, y[i])
    categorable.save('categorizing_model.h5')

    # y_prob = categorable.predict( )
    # print y_prob
    # y_classes = y_prob.argmax(axis=-1)
    # print y_classes


# yes = [[CatorableSample(c).vecs for c in temp_data], [CatorableSample(c).yes for c in temp_data]]
# rel_model = relevent_model()
# rel_model.fit(yes[0], yes[1])


# for i in cdata[0]:
#     for c in i["data"]:
#         CatorableSample(c)

crdata = [data["criteria"] for data in dadata]

# criteria data



get_time(t).final()
