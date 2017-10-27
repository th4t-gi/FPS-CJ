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

class FPS_data(object):
    """Documentation for FPS_data. 'Core' data object used in packet analysis"""

    def __init__(self, section, text, num=None):
        super(FPS_data, self).__init__()
        self.sect = section.lower() #UP, problem, Criteria etc.
        self.core = text
        self.num = num #This does not apply to UP, AP
        self.misc = ["up", "criteria", "apply criteria", "ap"]
        self.data = None

        if self.sect in self.misc:
            self.core = self.find_section(self.core, self.sect)
            # self.data =


        if self.sect == "problem" or self.sect == "solution":
            self.data = self.pos_cata("num", num)

    def find_section(self, group, section):
        name = re.search(r'(%s(?:\: (\d))?)' % section, group, flags=re.I)
        sect = re.search(r'(\(%s\) (\n?.+)+)' % name.group(1), group, flags=re.M)
        return sect.group(1)

    def pos_cata(self, mode, para): #f stands for the file; para is the paragraph to find keywords in
        paragraph_nums = re.findall(r"(\d+)\. \(", self.core)
        paragraph_nums = [int(num) for num in paragraph_nums]

        if mode == "num": #mode for finding judges decision
            dup = re.search(r"^{0}\. \(cata: (D) -> (\d+)\.\)".format(para), self.core, re.M)
            if dup: return [para, {dup.group(1): int(dup.group(2))}]

            pos = re.search(r"{0}\. \(cata: (\d+|P)(?:\, (\d+))?\)".format(para), self.core)
            if pos.group(2): return [para, get_cata_from([pos.group(1), pos.group(2)])]
            return [para, get_cata_from(pos.group(1))]

        if mode == "named": #mode for finding keywords from each problem
            paragraphs = re.split(r"\d+\. \(.*?\) ", self.core)
            paragraphs = [item.replace("\n", '') for item in paragraphs
                        if not item.startswith("#")]
            analysis = []
            for idx, p in enumerate(paragraphs):
                p = p.replace(".", '').replace(",", '').split()
                keywords = [get_cata_from(word) for word in p if get_cata_from(word)]
                if keywords and not para:
                    if len(keywords) == 1: keywords = keywords[0]
                    analysis.append([paragraph_nums[idx], keywords])

                elif para == idx + 1:
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

probs = open("Packet/ex_problems.txt").read()
sols = open("Packet/ex_solutions.txt").read()
misc = open("Packet/ex_UP+AP+S_Criteria+A_Criteria.txt").read()

UP = FPS_data("UP", misc)
prob_cata = []
sol_cata = []
for i in range(1, 17):
    prob_cata.append(FPS_data("problem", probs, i))
    sol_cata.append(FPS_data("solution", sols, i))
