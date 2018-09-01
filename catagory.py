from multi_key_dict import multi_key_dict
import re

catagories = {
    ("Arts & Aesthetics", 1) : ['public', 'art', 'arts', 'aesthetics', 'design', 'picture', 'drawing'],
    ("Basic Needs", 2) : ['poverty', 'food', 'shelter', 'water', 'basic needs', 'eat', 'humans', 'animals'],
    ("Business & Commerce", 3) : ['money', 'cash', 'stock', 'business', 'commerce', 'pay', 'fund', 'land'],
    ("Communication", 4) : ['information', 'communication', 'talking', 'phones', 'connection', 'discuss',
        'tell'],
    ("Defense", 5) : ['control', 'country', 'national', 'countries', 'protect', 'military', 'world', 'war'],
    ("Economics", 6) : ['economics', 'banking', 'bank', 'credit', 'credit card', 'money'],
    ("Education", 7) : ['education', 'educating', 'educate', 'school', 'learn', 'teach', 'math', 'science'],
    ("Environment", 8) : ['environment', 'plants', 'trees', 'animals', 'pollution', ],
    ("Ethics & Religion", 9) : ['moral', 'right and wrong', 'standards', 'belief', 'religion', 'ethics', 'god'],
    ("Government & Politics", 10) : ['government', 'politics', 'countries', 'senate', 'law',
        'house of representatives', 'prime minister'],
    ("Law & Justice", 11) : ['law', 'justice', 'court', 'senate', 'judge'],
    ("Misc", 12) : ['dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space'],
    ("Physical Health", 13) : ['physical health', 'hospital', 'hospitals', 'injury', 'injuries'],
    ("Psychological Health", 14) : ['counseling', 'therapy', 'phycological', 'health', 'crazy', 'mind',
        'mental health'],
    ("Recreation", 15) : ['enjoyment', 'activity', 'pastime', 'relaxation', 'recreation'],
    ("Social Relationships", 16) : ['social', 'relationship', 'individuals', 'agreement', 'agreeing'],
    ("Technology", 17) : ['technology', 'computers', 'algorithms', 'innovations', 'electricity',
        'machinery', 'dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space', 'materials', 'plastic'],
    ("Transportation", 18) : ['transportation', 'cars', 'trains', 'airplanes', 'movement', 'vehicle', 'spaceship']
}
multi_cata = multi_key_dict(catagories)

# probs = open("Q J102 Packet/ex_problems.txt").read()
# sols = open("Q J102 Packet/ex_solutions.txt").read()
# misc = open("Q J102 Packet/ex_misc.txt").read()

class FPS(object):
    """Documentation for FPS data object. 'Core' data object used in packet
    analysis"""

    def __init__(self, section, text, num=None):
        super(FPS, self).__init__()
        self.sect = section.lower() #UP, problem, Criteria etc.
        self.core = text
        self.num = num #This does not apply to UP, AP
        self.misc = {"up": self.pos_cata, "criteria": self._SCedit,
                    "apply criteria": self._ACedit, "ap": self.pos_cata}

        if self.sect in self.misc.keys():
            self.findSection(self.core, re.compile(r'(\(%s(?:\:(?: \d\,?)+)?\))' % self.sect, re.I))
            self.misc[self.sect]()

        if self.sect == "problem" or self.sect == "solution":
            self.findSection(self.core, re.compile(r"%d\. \(cata: (?:\d+|P|W|S|D .*?)(?:\, \d+)?(?:\; (Y|Y, O|R|E|R, E))?\)" % self.num))
            self.data = self.pos_cata()

        # if __name__ == '__main__':
        #     print self.core
        #     print self.data

    def findSection(self, group, name_pat):
        self.raw = name_pat.search(group).group()
        text = re.search(r"%s\s?(?:\n?.+)+" % re.escape(self.raw), group)
        self.core = text.group()

    def _SCedit(self):
        data = re.findall(r"(\d+)\. ([A-Z ]+)", self.core, re.I)
        self.data = [tuple([int(tup[0]), tup[1]]) for tup in data]
    def _ACedit(self):
        core = self.core.split("\n")[1:self.num]
        pattern = re.compile(r"sol: (\d+)\, \"([\w\. ]+)\"\)\[((?:\d: \d\,? ?)+)")
        for i in range(0, len(core)):
            core[i] = list(pattern.findall(core[i])[0])
            core[i][0] = int(core[i][0])
            core[i][2] = re.findall(r"\d: (\d)", core[i][2])
            core[i][2] = [dict(((idx + 1, val),)) for idx, val in enumerate(core[i][2])]
        self.data = core
    def pos_cata(self, mode='num'):
        if self.sect == "up": self.UAP()
        elif self.sect == "ap": self.UAP()

        elif mode == "num": #mode for finding judges decision
            dup = re.search(r"^{0}\. \(cata: (D) -> (\d+)\.\)".format(self.num), self.core, re.M)
            if dup: return [self.num, {dup.group(1): int(dup.group(2))}]

            pos = re.search(r"\(cata: (\d+|P|W|S|D .*?)(?:\, (\d+))?(?:\; (Y|Y, O|R|E|R, E))?\)", self.core)
            self.raw = pos.group()
            pos3 = pos.group(3)
            if pos3 and len(pos3) > 1:
                pos3 = pos3.split(', ')
            if pos.group(2): return [self.num, pos3, self.get_cata_from([pos.group(1), pos.group(2)])]
            if pos3: return [self.num, pos3, self.get_cata_from(pos.group(1))]
            return [self.num, self.get_cata_from(pos.group(1))]

    def get_cata_from(self, val):
        if val == "P": return val

        if type(val) == str:
            if re.match(r"\d+", val):
                cata = [multi_cata.keys()[idx] for idx, key in
                    enumerate(multi_cata.keys()) if key[1] == int(val)]
            else:
                cata = [multi_cata.keys()[multi_cata.values().index(l)]
                        for l in multi_cata.values() if val in l]

        elif type(val) == list:
            cata = [[multi_cata.keys()[idx] for idx, key in
                    enumerate(multi_cata.keys()) if key[1] == int(elmt)][0] for elmt in val]

        if len(cata) >= 2:
            return sorted(cata)
        elif len(cata) == 1:
            return cata[0]

    def UAP(self):
        process = re.search(r"\((?:UP|AP)\: ((?:\d\,? ?)+)\)", self.raw)
        self.data = [int(i) for i in process.group(1).split(", ")]

# prob_cata = [FPS("problem", probs, i) for i in range(1, 17)]
# UP = FPS("UP", misc)
# sol_cata = [FPS("solution", sols, i) for i in range(1, 17)]
# SC = FPS("Criteria", misc)
# AC = FPS("Apply Criteria", misc)
# AP = FPS("AP", misc)
