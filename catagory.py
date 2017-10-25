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
    ("Government & Politics", 10) : ['government', 'politics', 'countries', 'senate', 'law', 'house of representatives'],
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

# class FPS_data(type):
#     """Documentation for FPS_data. 'Core' of data used in packet analysis"""
#     def __init__(self, section, text, num=None):
#         super(FPS_data, self).__init__()
#         self.sect = section #AP, UP, problem, etc.
#         self.num = num #This does not apply to UP, AP
#         self.core = text
#         self.misc = ["UP", "Criteria", "Apply Criteria", "AP"]
#
#         if self.sect in self.misc:
#             self.core = self.find_section(self.core, self.sect)
#
#         if self.sect == "problem" or self.sect == "solution":
#
#
#     def find_section(self, group, section):
#         name = re.search(r'(?P<name>%s(: \d)?)' % section, group)
#         sect = re.search(r'(\(%s\)(\n?.+)+)' % name.group("name"), group, re.M)
#         return sect.group(1)

def pos_cata(f): #f stands for the file
    pos = re.findall(r"(\d+\.) \(cata\: (?:(\d+)|(\d+)\,\s(\d+)|)\)", f)
    analysis = [tuple([el for el in tup if el]) for tup in pos]
    print analysis

    # i = 1
    # for each_prob in analysis:
    #     if len(each_prob) == 1:
    #         each_prob = [item for sublist in each_prob for item in sublist]
    #     for idx, cata in enumerate(each_prob):
    #         if len(cata) == 1:
    #             each_prob[idx] = tuple([item for sublist in cata for item in sublist])
    #
    #     each_prob.insert(0, str(i) + '.')
    #     if len(each_prob) > 1:
    #         rtrn.append(each_prob)
    #     i += 1
    # return rtrn


def get_key_from_list(val, dictionary):
    try:
        d = multi_key_dict(dictionary)
        cata = [d.keys()[d.values().index(l)]
                for l in d.values() if val in l]
        return sorted(cata)
    except Exception:
        print """KeyError: Keys of dictionary must be of type tup not {0}.
        """.format(type(dictionary).__name__)
        exit()

# def clean_up(group):
#     group = group.replace(',', '').replace('.', '')
#     group = re.split(r'\n\n', group)
#     for string in group:
#         if string.startswith("#"):
#             group.remove(string)
#
#     return group

probs = open("Packet/ex_problems.txt").read()
# print probs
# probs = clean_up(probs)
# print "\n", probs
# sols = clean_up(open("Packet/ex_solutions.txt").read())
misc = open("Packet/ex_UP+AP+S_Criteria+A_Criteria.txt").read()
# UP = find_section(misc, "UP")
# AP = find_section(misc, "AP")
# SC = find_section(misc, "Criteria")
# AC = find_section(misc, "Apply Criteria")
# print AC
# for line in AP:
#     print line
prob_cata = pos_cata(probs)
# print "\n", prob_cata
# sol_cata = pos_cata(sols)
# for sol in sol_cata:
#     for item in sol:
#         print item
