import os, re
from catagory import FPS, find_packet
# from nn.CANN import CataNN

#lowercases every element in a given list
def integrity(list):
    _list = []
    for i in list:
        _list.append(i.lower())
    return _list

#finds the directory path of given folder

packet = raw_input("folder name of packet: ").upper()
if not packet:
    packet = "CO-15-16-J102-S"
flashdrive = raw_input("Is the file on a USB drive?(yes/no): ")

if flashdrive == "yes":
    flashdrive = raw_input("What is the name of the USB drive?: ")
    if flashdrive.lower() in integrity(os.listdir("/Volumes")):
        os.chdir("/Volumes/{}".format(flashdrive))
        packet_path = find_packet(packet, os.getcwd())
else:
    print "OK"
    packet_path = find_packet(packet, "~/")
    packet_path = ''.join(re.split(re.compile(r"({})".format(packet)), packet_path)[:2]) + "/"

try:
    probs = [open(packet_path + i).read() for i in os.listdir(packet_path) if 'prob' in i]
    sols = [open(packet_path + i).read() for i in os.listdir(packet_path) if 'sol' in i]
    misc = [open(packet_path + i).read() for i in os.listdir(packet_path) if 'up' in i]
except OSError:
    print "invalid packet directory: {}".format(packet)
    quit()
except IndexError:
    print "packet file(s) not found"

# prob1 = FPS("problem", probs, 1)
# prob_cata = [FPS("problem", probs, i) for i in range(1, 17)]
# sol_cata = [FPS("solution", sols, i) for i in range(1, 17)]
# UP = FPS("UP", misc)
# SC = FPS("Criteria", misc)
# AC = FPS("grid", misc)
# AP = FPS("AP", misc)

num = 4
# p0 = CataNN([18], prob_cata[num].core, prob_cata[num].data)
# pnn = [CataNN([18], i.core, i.data) for i in prob_cata]


total_points = 0
