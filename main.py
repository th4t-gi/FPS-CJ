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

def catagorize(text):
    def takeSecond(elem):
        return elem[1]
    if not isinstance(text, list):
        text = text.split()

    pos = [(list(sorted(catagories.keys())).index(key))
            for key in catagories.keys()
            for i in catagories[key] if i in text]
    s = sorted(pos, key=pos.count, reverse=True)
    r = [[i, s.count(i)] for i in list(set(s))]
        #if s.count(i) >= 1 or len(s) == 1
    r.sort(key=takeSecond, reverse=True)
    most = 0
    for i in r:
        if i[1] > most:
            most = i[0]

    other = []
    for i in r:
        for j in range(i[1]):
            other.append(i[0])
    dic = {
            "most" : most,
            "all" : other
        }
    return dic

# sampleing(True, ["food", "public", "money", "cash", "arts", 'hospital', 'commerce', 'drawing'])
sampleing("problem")
