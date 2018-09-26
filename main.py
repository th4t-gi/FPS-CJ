import time
t = time.time()
import os, re, json, subprocess, warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import format
from nn.grading import framework

p = format.get_packet()
packet = p[0]
paths = p[1]

for i, val in enumerate(paths):
    fuzzy = format.find_packet("fuzzy.txt", re.sub(r"data-\d{3}\.json", "", paths[i]).replace(" ", "\\ "), dir=False)
    jeff = open(paths[i]).read()
    with open(val, "r+") as f:
        f.write(re.sub(r"future-scene\": \".*?\"", "future-scene\": \"{}\"".format(fuzzy),
                re.sub(r"data-filepath\": \".*?\"", "data-filepath\": \"{}\"".format(val), jeff)))

dadata = [json.loads(open(i).read()) for i in paths]
d = [list(format.text(r".*?text", data)) for data in dadata]
vecs = format.word2vec(d, packet)


#    Neural
#    Network
#     Stuff

print "time:", round(time.time()- t, 3)
