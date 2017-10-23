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

class FPS_data(type):
    """Documentation for FPS_data. Core of data used in packet analysis"""


def get_key_from_list(val, dictionary):
    d = multi_key_dict(dictionary)
    cata = [d.keys()[d.values().index(l)]
            for l in d.values() if val in l]
    return sorted(cata)


def clean_up(group):
    group = group.replace(',', '').replace('.', '')
    group = re.split(r'\n\n', group)
    for string in group:
        if string.startswith("#"):
            group.remove(string)

    return group

def find_section(group, section):
    go = re.search(r'(?P<name>%s(: \d)?)' % section, group)
    # sect = []
    sect = re.search(r'(\(%s\)(\n?.+)+)' % go.group("name"), group, re.M)
    return sect.group(1)

def pos_cata(f):
    analysis = []
    rtrn = []
    for problem in f:
        words = []
        for word in problem.split():
            cata = get_key_from_list(word, catagories)
            if cata:
                words.append(cata)
        analysis.append(words)

    i = 1
    for each_prob in analysis:
        if len(each_prob) == 1:
            each_prob = [item for sublist in each_prob for item in sublist]
        for idx, cata in enumerate(each_prob):
            if len(cata) == 1:
                each_prob[idx] = tuple([item for sublist in cata for item in sublist])

        each_prob.insert(0, str(i) + '.')
        if len(each_prob) > 1:
            rtrn.append(each_prob)
        i += 1
    return rtrn

probs = clean_up(open("Packet/ex_problems.txt").read())
sols = clean_up(open("Packet/ex_solutions.txt").read())
misc = open("Packet/ex_UP+AP+S_Criteria+A_Criteria.txt").read()
bla = FPS_data(12)
# UP = find_section(misc, "UP")
# AP = find_section(misc, "AP")
# SC = find_section(misc, "Criteria")
AC = find_section(misc, "Apply Criteria")
print AC
# for line in AP:
#     print line
# prob_cata = pos_cata(probs)
# sol_cata = pos_cata(sols)
# for sol in sol_cata:
#     for item in sol:
#         print item
