# from multi_key_dict import multi_key_dict
import re, sys, subprocess, time, os

def find_packet(packet, rootdir):
    try:
        _packet_path = subprocess.check_output("find {} -type d -name \"{}\" -print".format(rootdir, packet),shell=True,stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        _packet_path = e.output
    if not _packet_path.endswith("/"):
        _packet_path = _packet_path.replace('\n', '')
    return _packet_path

# catagories = {
#     ("Arts & Aesthetics", 1) : ['public', 'art', 'arts', 'aesthetics', 'design', 'picture', 'drawing'],
#     ("Basic Needs", 2) : ['poverty', 'food', 'shelter', 'water', 'basic needs', 'eat', 'humans', 'animals'],
#     ("Business & Commerce", 3) : ['money', 'cash', 'stock', 'business', 'commerce', 'pay', 'fund', 'land'],
#     ("Communication", 4) : ['information', 'communication', 'talking', 'phones', 'connection', 'discuss',
#         'tell'],
#     ("Defense", 5) : ['control', 'country', 'national', 'countries', 'protect', 'military', 'world', 'war'],
#     ("Economics", 6) : ['economics', 'banking', 'bank', 'credit', 'credit card', 'money'],
#     ("Education", 7) : ['education', 'educating', 'educate', 'school', 'learn', 'teach', 'math', 'science'],
#     ("Environment", 8) : ['environment', 'plants', 'trees', 'animals', 'pollution', ],
#     ("Ethics & Religion", 9) : ['moral', 'right and wrong', 'standards', 'belief', 'religion', 'ethics', 'god'],
#     ("Government & Politics", 10) : ['government', 'politics', 'countries', 'senate', 'law',
#         'house of representatives', 'prime minister'],
#     ("Law & Justice", 11) : ['law', 'justice', 'court', 'senate', 'judge'],
#     ("Misc", 12) : ['dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space'],
#     ("Physical Health", 13) : ['physical health', 'hospital', 'hospitals', 'injury', 'injuries'],
#     ("Psychological Health", 14) : ['counseling', 'therapy', 'phycological', 'health', 'crazy', 'mind',
#         'mental health'],
#     ("Recreation", 15) : ['enjoyment', 'activity', 'pastime', 'relaxation', 'recreation'],
#     ("Social Relationships", 16) : ['social', 'relationship', 'individuals', 'agreement', 'agreeing'],
#     ("Technology", 17) : ['technology', 'computers', 'algorithms', 'innovations', 'electricity',
#         'machinery', 'dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space', 'materials', 'plastic'],
#     ("Transportation", 18) : ['transportation', 'cars', 'trains', 'airplanes', 'movement', 'vehicle', 'spaceship']
# }
# multi_cata = multi_key_dict(catagories)

if __name__ == '__main__':
    from catagory import FPS
    ttime = time.time()
    packet = sys.argv[1]
    packet_path = ''.join(re.split(re.compile(r"({})".format(packet)), find_packet(packet, "~/"))[:2]) + "/"
    try:
        probs = [open(packet_path + i).read() for i in os.listdir(packet_path) if 'prob' in i]
    except OSError:
        print "invalid packet directory: {}".format(packet)
        quit()
    except IndexError:
        print "packet file(s) not found"

    prob1 = FPS("problem", probs, 1)


    ttime = time.time() - ttime
    print "time:", round(ttime, 2)


class FPS(object):
    """Documentation for FPS data object. 'Core' data object used in packet
    analysis"""

    def __init__(self, section, text, num=None):
        super(FPS, self).__init__()
        self.sect = section.lower() #UP, problem, Criteria etc.
        self.core = text
        self.num = num #This does not apply to UP, AP
        if type(self.core) is list:
            self.datdata = [self.cratdatdata(i) for i in self.core]
        else:
            self.datdata = self.cratdatdata(self.core)
        print self.datdata

        # self.misc = {"up": self.datdata.up, "criteria": self.datdata.criteria,
        #             "grid": self.datdata.grid, "ap": self.datdata.ap}


        # if self.sect == "problem" or self.sect == "solution":
        #     self.findSection(self.core, re.compile(r"%d\. \(cata: (?:\d+|P|W|S|D .*?)(?:\, \d+)?(?:\; (Y|Y, O|R|E|R, E))?\)" % self.num))
        #     self._data = self.pos_cata()
        # else:
        #     self.findSection(self.core, re.compile(r'(\(%s(?:\:(?: \d{1,2}\,?)+)?\))' % self.sect, re.I))
        #     self.misc[self.sect]()

    def cratdatdata(self, core):
        return FPS.data(self, core)

    class data(object):

        def __init__(self, oi, core):
            self.score = None
            self.out = oi
            self.core = core
            self.sectext = self.findSection(self.core, re.compile(r"%d\. \(cata: (?:\d+|P|W|S|D .*?)(?:\, \d+)?(?:\; (Y|Y, O|R|E|R, E))?\)" % self.out.num))

        def up(self):
            pass
        def criteria(self):
            pass
        def grid(self):
            pass
        def ap(self):
            pass

        def findSection(self, group, name_pat):
            self.raw = name_pat.search(group).group()
            text = re.search(r"%s\s?(?:\n?.+)+" % re.escape(self.raw), group)
            return text.group()

    # def _SCedit(self):
    #     data = re.findall(r"(\d+)\. ([A-Z ]+)", self.core, re.I)
    #     self._data = [tuple([int(tup[0]), tup[1]]) for tup in data]
    #
    # def _ACedit(self):
    #     core = self.core.split("\n")[1:self.num]
    #     pattern = re.compile(r"sol: (\d+)\, \"(.+?)\"\)\[((?:\d: \d\,? ?)+)")
    #     for i in range(0, len(core)):
    #         core[i] = list(pattern.findall(core[i])[0])
    #         core[i][0] = int(core[i][0])
    #         core[i][2] = re.findall(r"\d: (\d)", core[i][2])
    #         core[i][2] = [dict(((idx + 1, val),)) for idx, val in enumerate(core[i][2])]
    #     self._data = core
    #
    # def pos_cata(self, mode='num'):
    #     if self.sect == "up": self.UAP()
    #     elif self.sect == "ap": self.UAP()
    #
    #     elif mode == "num": #mode for finding judges decision
    #         dup = re.search(r"^{0}\. \(cata: (D) -> (\d+)\.\)".format(self.num), self.core, re.M)
    #         if dup: return [self.num, {dup.group(1): int(dup.group(2))}]
    #
    #         if self.sect == "problem":
    #             self._clar = re.search(r"\(clarity\: (\d{1,2})\)", self._core)
    #             self.clar = self._clar.group(1)
    #
    #         raw = re.compile(r"\(cata: (\d+|P|W|S|D .*?)(?:\, (\d+))?(?:\; (Y|Y, O|R|E|R, E))?\)")
    #         pos = re.search(raw, self.core)
    #         self.raw = pos.group()
    #         pos3 = pos.group(3)
    #         if pos3 and len(pos3) > 1:
    #             pos3 = pos3.split(', ')
    #         if pos.group(2): return [self.num, pos3, self.get_cata_from([pos.group(1), pos.group(2)])]
    #         if pos3: return [self.num, pos3, self.get_cata_from(pos.group(1))]
    #         return [self.num, self.get_cata_from(pos.group(1))]
    #
    # def get_cata_from(self, val):
    #     if val == "P": return val
    #
    #     if type(val) == str:
    #         if re.match(r"\d+", val):
    #             cata = [multi_cata.keys()[idx] for idx, key in
    #                 enumerate(multi_cata.keys()) if key[1] == int(val)]
    #         else:
    #             cata = [multi_cata.keys()[multi_cata.values().index(l)]
    #                     for l in multi_cata.values() if val in l]
    #
    #     elif type(val) == list:
    #         cata = [[multi_cata.keys()[idx] for idx, key in
    #                 enumerate(multi_cata.keys()) if key[1] == int(elmt)][0] for elmt in val]
    #
    #     if len(cata) >= 2:
    #         return sorted(cata)
    #     elif len(cata) == 1:
    #         return cata[0]
    #
    # def UAP(self):
    #     process = re.search(r"\((?:UP|AP)\: ((?:\d\,? ?)+)\)", self.raw)
    #     self._data = [int(i) for i in process.group(1).split(", ")]
