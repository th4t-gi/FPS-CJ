import time
t = time.time()
import os, re, json, subprocess, warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import format
from nn.CANN import CataNN
#lowercases every element in a given list
def integrity(list):
    _list = []
    for i in list:
        _list.append(i.lower())
    return _list


packet = "CO-18-M205-S"#raw_input("folder name of packet: ").upper()
flashdrive = "no" #raw_input("Is the file on a USB drive?(yes/no): ")

if flashdrive == "yes":
    flashdrive = raw_input("What is the name of the USB drive?: ")
    if flashdrive.lower() in integrity(os.listdir("/Volumes")):
        os.chdir("/Volumes/{}".format(flashdrive))
        packet_path = format.find_packet(packet, os.getcwd())
elif packet:
    print "OK"
    packet_path = format.find_packet(packet, "~/Code/")
    packet_path = ''.join(re.split(re.compile(r"({})".format(packet)), packet_path)[:2]) + "/"

try:
    if not packet:
        paths = subprocess.check_output("find ~/Code/ -regex \".*/data-[0-9][0-9][0-9]\.json\" -type f",shell=True,stderr=subprocess.STDOUT)
        paths = paths.split("\n")

    else:
        paths = [packet_path + i for i in os.listdir(packet_path) if 'data' in i]
except OSError:
    print "invalid packet directory: {}".format(packet)
    quit()
except IndexError: print "packet file(s) not found"
except subprocess.CalledProcessError as e:
    paths = e.output

dadata = []
for i in [i for i in paths if i]:
    with open(i) as file:
        f = json.loads(file.read())
        dadata.append(f)

d = []
comments = []
for data in dadata:
    d.append(list(format.text(r".*?text", data)))
    comments.append(list(format.text(r"comments|feedback", data)))

vecs = format.word2vec(d)

num = 4
# p0 = CataNN([18], prob_cata[num].core, prob_cata[num].data)
# pnn = [CataNN([18], i.core, i.data) for i in prob_cata]


total_points = 0
print time.time()- t
