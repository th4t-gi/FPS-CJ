sample = [1, 2, 4, 5, 7, 10, 13, 16]
place = [3, 6, 8, 9, 11, 12, 14, 15]
from catagory import catagorize
from random import randint


def sampleing(name, up=None):
    for i in range(2):
        re = randint(0, len(sample) - 1)
        sample[re] = place[re]

    cata = []
    for x in sample:
        try:
            data = catagorize(raw_input("Type the #%d %s: " % (x, name)))
            cata.append(data["most"])
            per = float(data["all"].count(data["most"])) / len(data["all"])
        except ZeroDivisionError:
            print "There was no catagory found"
            continue
        s = "the #%d %s was in the number %d catagory with " % (x, name, data["most"])
        print s + str(round(per * 100, 3)) + r"% certainty"
    if name == "solution":
        catanum = catagorize(up)
        print catanum
# sampleing(True, ["food", "public", "money", "cash", "arts", 'hospital', 'commerce', 'drawing'])
sampleing("problem")
