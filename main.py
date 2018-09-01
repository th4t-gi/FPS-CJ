from os import listdir
from catagory import FPS
from nn.CANN import CataNN


packet = "q j102 packet/"#raw_input("path to packet files: ") + '/'
def find(keyword, array):
    return [i for i in array if keyword in i][0]
try:
    probs = open(packet + find('prob', listdir(packet))).read()
    sols = open(packet + find('sol', listdir(packet))).read()
    misc = open(packet + find('misc', listdir(packet))).read()
except OSError:
    print("invalid packet directory")
    quit()

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
