from multi_key_dict import multi_key_dict
import re

catagories = {
    ("Arts & Aesthetics", 1) : ['public', 'art', 'arts', 'aesthetics', 'design', 'picture', 'drawing'],
    ("Basic Needs", 2) : ['poverty', 'food', 'shelter', 'water', 'basic needs'],
    ("Business & Commerce", 3) : ['money', 'cash', 'stock', 'business', 'commerce'],
    ("Communication", 4) : ['information', 'communication', 'talking', 'phones', 'connection', 'discuss',
        'tell'],
    ("Defense", 5) : ['control', 'country', 'national', 'countries', 'protect', 'military'],
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
        'machinery', 'dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space'],
    ("Transportation", 18) : ['transportation', 'cars', 'trains', 'airplanes', 'movement', 'vehicle']
}
multi_cata = multi_key_dict(catagories)

class FPS(object):
    """Documentation for FPS data object. 'Core' data object used in packet
    analysis"""

    def __init__(self, section, text, num=0):
        super(FPS, self).__init__()
        self.sect = section.lower() #UP, problem, Criteria etc.
        self.core = text
        self.num = num #This does not apply to UP, AP
        self.misc = {"up": self.pos_cata, "criteria": self._SCedit,
                    "apply criteria": self._ACedit, "ap": self.pos_cata}

        if self.sect in self.misc.keys():
            self.core = self._findSection(self.core,
                re.compile(r'(\(%s(?:\: \d)?\))' % self.sect, re.I))
            self.data = self.misc[self.sect](text=self.sect)

        if self.sect == "problem" or self.sect == "solution":
            self.core = self._findSection(self.core,
                re.compile(r"%d\. \(cata: (?:\d+|P|D .*?)(?:\, \d+)?\)" % self.num))
            self.data = self.pos_cata("num")

    def _findSection(self, group, name_pat):
        name = name_pat.search(group)
        sect = re.search(r"%s\s?(?:\n?.+)+" % re.escape(name.group()), group)
        return sect.group()

    def _SCedit(self, text):
        data = re.findall(r"(\d+)\. ([A-Z ]+)", self.core, re.I)
        return [tuple([int(tup[0]), tup[1]]) for tup in data]
    def _ACedit(self, text):
        core = self.core.split("\n")[1:]
        pattern = re.compile(r"sol: (\d+)\, \"([\w\. ]+)\"\)\[((?:\d: \d\,? ?)+)")
        for i in range(0, len(core)):
            core[i] = list(pattern.findall(core[i])[0])
            core[i][0] = int(core[i][0])
            core[i][2] = re.findall(r"\d: (\d)", core[i][2])
            core[i][2] = [dict(((idx + 1, val),)) for idx, val in enumerate(core[i][2])]
        return core
    def pos_cata(self, mode='num', text=None):
        if text == "up":
            prob = re.search(r"\(UP: (\d+)\)", self.core).group(1)
            # prob_cata[int(prob) - 1].data.insert(0, 'UP')
            return prob_cata[int(prob) - 1].data
        elif text == "ap":
            sol = re.search(r"\(AP: (\d+)\)", self.core).group(1)
            # sol_cata[int(sol) - 1].data.insert(0, 'AP')
            return sol_cata[int(sol) - 1].data

        if mode == "num": #mode for finding judges decision
            dup = re.search(r"^{0}\. \(cata: (D) -> (\d+)\.\)".format(self.num), self.core, re.M)
            if dup: return [self.num, {dup.group(1): int(dup.group(2))}]

            pos = re.search(r"\(cata: (\d+|P)(?:\, (\d+))?\)", self.core)
            if pos.group(2): return [self.num, get_cata_from([pos.group(1), pos.group(2)])]
            return [self.num, get_cata_from(pos.group(1))]

        if mode == "named": #mode for finding keywords from each problem
            paragraphs = re.split(r"\d+\. \(.*?\) ", self.core)
            paragraphs = [item.replace("\n", '') for item in paragraphs
                        if not item.startswith("#")]
            analysis = []
            for idx, p in enumerate(paragraphs):
                p = p.replace(".", '').replace(",", '').split()
                keywords = [get_cata_from(word) for word in p if get_cata_from(word)]
                if keywords and not self.num:
                    if len(keywords) == 1: keywords = keywords[0]
                    analysis.append([idx+1, keywords])

                elif self.num == idx + 1:
                    keywords = [get_cata_from(word) for word in p if get_cata_from(word)]
                    if not keywords: return "No keywords found"
                    return keywords
            return analysis


def get_cata_from(val):
    if val == "P":
        return val

    if type(val) == str:
        if re.match(r"\d+", val):
            cata = [multi_cata.keys()[idx] for idx, key in
                enumerate(multi_cata.keys()) if key[1] == int(val)]
        else:
            cata = [multi_cata.keys()[multi_cata.values().index(l)]
                    for l in multi_cata.values() if val in l]

    elif type(val) == list:
        cata = []
        for elmt in val:
            cata.append([multi_cata.keys()[idx] for idx, key in
                    enumerate(multi_cata.keys()) if key[1] == int(elmt)][0])

    if len(cata) >= 2:
        return sorted(cata)
    elif len(cata) == 1:
        return cata[0]

probs = open("Code/Project Folder/FPS/Packet/ex_problems.txt").read()
sols = open("Code/Project Folder/FPS/Packet/ex_solutions.txt").read()
misc = open("Code/Project Folder/FPS/Packet/ex_UP+AP+S_Criteria+A_Criteria.txt").read()
# 
# prob_cata = [FPS("problem", probs, i) for i in range(1, 17)]
# UP = FPS("UP", misc)
# sol_cata = [FPS("solution", sols, i) for i in range(1, 17)]
# SC = FPS("Criteria", misc)
# AC = FPS("Apply Criteria", misc)
# AP = FPS("AP", misc)
