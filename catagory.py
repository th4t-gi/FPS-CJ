from multi_key_dict import multi_key_dict
import re

catagories = {
    ("Arts & Aesthetics", 1) : ['public', 'art', 'arts', 'aesthetics', 'design', 'picture', 'drawing'],
    ("Basic Needs", 2) : ['poverty', 'food', 'shelter', 'water', 'basic needs'],
    ("Business & Commerce", 3) : ['money', 'cash', 'stock', 'business', 'commerce'],
    ("Communication", 4) : ['information', 'communication', 'talking', 'phones', 'connection', 'discuss', 'tell'],
    ("Defense", 5) : ['control', 'country', 'national', 'countries', 'protect', 'military'],
    ("Economics", 6) : ['economics', 'banking', 'bank', 'credit', 'credit card', 'money'],
    ("Education", 7) : ['education', 'educating', 'educate', 'school', 'learn', 'teach', 'math', 'science'],
    ("Environment", 8) : ['environment', 'plants', 'trees', 'animals', 'pollution', ],
    ("Ethics & Religion", 9) : ['moral', 'right and wrong', 'standards', 'belief', 'religion', 'ethics', 'god'],
    ("Government & Politics", 10) : ['government', 'politics', 'countries', 'senate', 'law', 'house of representatives',
        'prime minister'],
    ("Law & Justice", 11) : ['law', 'justice', 'court', 'senate', 'judge'],
    ("Misc", 12) : ['dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space'],
    ("Physical Health", 13) : ['physical health', 'hospital', 'hospitals', 'injury', 'injuries'],
    ("Psychological Health", 14) : ['counseling', 'therapy', 'phycological', 'health', 'crazy', 'mind', 'mental health'],
    ("Recreation", 15) : ['enjoyment', 'activity', 'pastime', 'relaxation', 'recreation'],
    ("Social Relationships", 16) : ['social', 'relationship', 'individuals', 'agreement', 'agreeing'],
    ("Technology", 17) : ['technology', 'computers', 'algorithms', 'innovations', 'electricity',
        'machinery', 'dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space'],
    ("Transportation", 18) : ['transportation', 'cars', 'trains', 'airplanes', 'movement', 'vehicle']
}
multi_cata = multi_key_dict(catagories)

class FPS_data(type):
    """Documentation for FPS_data. 'Core' of data used in packet analysis"""
    def __init__(self, section, text, num=None):
        super(FPS_data, self).__init__()
        self.sect = section #UP, problem, Criteria etc.
        self.num = num #This does not apply to UP, AP
        self.core = text
        self.misc = ["up", "criteria", "apply criteria", "ap"]

        if self.sect.lower() in self.misc:
            self.core = self.find_section(self.core, self.sect)

        if self.sect.lower() == "problem" or self.sect.lower() == "solution":
            pass

    def find_section(self, group, section):
        name = re.search(r'(?P<name>%s(: \d)?)' % section, group)
        sect = re.search(r'(\(%s\)(\n?.+)+)' % name.group("name"), group, re.M)
        return sect.group(1)

def pos_cata(f, mode, para=None): #f stands for the file; para is the paragraph to find keywords in
    paragraph_nums = re.findall(r"(\d+)\. \(", f)
    paragraph_nums = [int(num) for num in paragraph_nums]

    if mode == "named":
        pos = re.findall(r"\d+\. \(cata: (\d+|P|D)(?:\, (\d+)| -> \d+\.)?\)", f)
        pos = [list(el) for el in zip(paragraph_nums, [list(tup) if tup[1] else tup[0] for tup in pos])]
        dup = re.findall(r"(\d+)\. \(cata: (D) -> (\d+)\.\)", f)
        dup = [[int(data[0]), dict((("D", int(data[2])),))] for data in dup]
        for each in pos:
            if type(each[1]) == list:
                each[1] = get_cata_from(each[1])
            elif each[1] == 'D':
                each[0:2] = [elmt for elmt in dup if each[0] == elmt[0]][0]
            elif not each[1] == 'P':
                each[1] = get_cata_from(int(each[1]))

        return pos

    if mode == "num":
        paragraphs = re.split(r"\d+\. \(.*?\) ", f)
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
    if type(val) == str:
        cata = [multi_cata.keys()[multi_cata.values().index(l)]
                for l in multi_cata.values() if val in l]
    elif type(val) == int:
        cata = [multi_cata.keys()[idx] for idx, key in
                enumerate(multi_cata.keys()) if key[1] == val]
    elif type(val) == list:
        cata = []
        for elmt in val:
            cata.append([multi_cata.keys()[idx] for idx, key in
                    enumerate(multi_cata.keys()) if key[1] == int(elmt)][0])
    if len(cata) >= 2:
        return sorted(cata)
    elif len(cata) == 1:
        cata = cata[0]
        return cata

probs = open("Packet/ex_problems.txt").read()
sols = open("Packet/ex_solutions.txt").read()
misc = open("Packet/ex_UP+AP+S_Criteria+A_Criteria.txt").read()

prob_cata = pos_cata(probs, "named")
sol_cata = pos_cata(sols, "named")
