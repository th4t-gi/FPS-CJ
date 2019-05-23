import time
t = time.time()
import os, re, json, subprocess, pickle, numpy as np, nltk
import math, string
from keras.preprocessing.sequence import pad_sequences
from sys import argv
from models import *
from format import *

np.set_printoptions(threshold=np.inf)
# LOAD DATA
p = Getpacket("ALL")
root = p.root.replace("\ ", " ")
#loads found json files and finds all text to be vectorized

dadata = [json.loads(open(i).read()) for i in p.paths]
dtext = [list(get_values(r".*?text", data)) for data in dadata]
#add the fuzzy text to become word vectors
for i, ptext in enumerate(dtext):
    ptext.append(open(root + dadata[i]["meta"]["computer"]["future-scene-filepath"]).read())

#Word2Vec alg applied and creates vecs
print(dtext)
tokens = tokenize(dtext)
vecs = vectorize(flat(tokens, 2), show=False, size=100)
dump_vectors(vecs, os.getcwd())

OGtokens = sorted(set(flat(tokens)))

#challenges data
cdata = [[data["challenges"], data["solutions"]] for data in dadata]

temp_data = flat([i["data"] for i in flat(cdata)])

x, y, = [], []

# training_cent = int(math.ceil(len(temp_data) * .9375))
for i, c in enumerate(temp_data):
    s = CatorableSample(c, vecs)
    x.append(s.vecs)
    y.append(np.reshape(s.c, (1, 22)))

batched = sorted([i.shape[0] for i in x])
pickle.dump(batched, open('batches.p', 'wb'))

x = pad_sequences(x, maxlen=batched[-1], padding='post', dtype='float32')
y = np.asarray(y, dtype=np.float32)

if 'train' in argv:
    # APPLY MODELS
    model = Categorizing_model()
    model.fit(x, y, epochs=10, batch_size=8, validation_split=0.125)

    # model.predict(x[-1])
# yes = [[CatorableSample(c).vecs for c in temp_data], [CatorableSample(c).yes for c in temp_data]]
# rel_model = relevent_model()
# rel_model.fit(yes[0], yes[1])


# for i in cdata[0]:
#     for c in i["data"]:
#         CatorableSample(c)

crdata = [data["criteria"] for data in dadata]

# criteria data



get_time(t).final()
