import os, re, subprocess
from catagory import FPS
from nn.CANN import CataNN


packet = raw_input("folder of packet: ").title()

try:
    packet_path = subprocess.check_output("find ~/Code/Project\ folder/ -type d -name \"{}\" -print".format(packet),shell=True,stderr=subprocess.STDOUT)
except subprocess.CalledProcessError as e:
    packet_path = e.output

if not packet_path.endswith("/"):
    packet_path = packet_path.replace('\n', '') + "/"
def find(array, keyword):
    return [i for i in array if keyword in i][0]

try:
    probs = open(packet_path + find(os.listdir(packet_path), 'prob')).read()
    sols = open(packet_path + find(os.listdir(packet_path), 'sol')).read()
    misc = open(packet_path + find(os.listdir(packet_path), 'up')).read()
except OSError:
    print "invalid packet directory"
    quit()
except IndexError:
    print "packet file names need to be Uncapitalized"

prob_cata = [FPS("problem", probs, i) for i in range(1, 17)]
# sol_cata = [FPS("solution", sols, i) for i in range(1, 17)]
UP = FPS("UP", misc)
# SC = FPS("Criteria", misc)
# AC = FPS("Apply Criteria", misc)
# AP = FPS("AP", misc)

num = 4
p0 = CataNN([18], prob_cata[num].core, prob_cata[num].data)
# pnn = [CataNN([18], i.core, i.data) for i in prob_cata]


total_points = 0

#------------------------------problems------------------------------


#---------------------------------UP---------------------------------


#-----------------------------solutions------------------------------


#------------------------------criteria------------------------------


#---------------------------apply criteria---------------------------


#---------------------------------AP---------------------------------
