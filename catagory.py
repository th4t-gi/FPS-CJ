from multi_key_dict import multi_key_dict
import re

catagories = {
    ("Arts & Aesthetics", 1) : ['public', 'art', 'arts', 'aesthetics', 'design', 'picture', 'drawing'],
    ("Basic Needs", 2) : ['poverty', 'food', 'shelter', 'water', 'basic needs'],
    ("Business & Commerce", 3) : ['money', 'cash', 'stock', 'business', 'commerce'],
    ("Communication", 4) : ['information', 'communication', 'talking', 'phones', 'connection'],
    ("Defense", 5) : ['control', 'country', 'national', 'countries'],
    ("Economics", 6) : ['economics', 'banking', 'bank', 'credit', 'credit card', 'money'],
    ("Education", 7) : ['education', 'educating', 'educate', 'school', 'learn', 'teach'],
    ("Environment", 8) : ['environment', 'plants', 'trees', 'animals', 'pollution'],
    ("Ethics & Religion", 9) : ['moral', 'right and wrong', 'standards', 'belief', 'religion', 'ethics', 'god'],
    ("Government & Politics", 10) : ['government', 'politics', 'countries', 'senate', 'law', 'house of representatives'],
    ("Law & Justice", 11) : ['law', 'justice', 'court', 'senate', 'judge'],
    ("Misc", 12) : ['dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space'],
    ("Physical Health", 13) : ['physical health', 'hospital', 'hospitals', 'injury', 'injuries'],
    ("Psychological Health", 14) : ['counseling', 'therapy', 'phycological', 'health', 'crazy', 'mind', 'mental health'],
    ("Recreation", 15) : ['enjoyment', 'activity', 'pastime', 'relaxation', 'recreation'],
    ("Social Relationships", 16) : ['social', 'relationship', 'individuals', 'agreement'],
    ("Technology", 17) : ['technology', 'computers', 'algorithms', 'innovations', 'electricity',
        'machinery', 'dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space'],
    ("Transportation", 18) : ['transportation', 'cars', 'trains', 'airplanes', 'movement', 'vehicle']
}

def get_key_from_listval(d, val):

    cata = []
    for l in d.values():
        if val in l:
            cata.append(catagories.keys()[catagories.values().index(l)][1])

    return sorted(cata)

def clean_up(group):
    if type(group) is str:
        group.translate(None, "\n")
    group = re.split("\d+\.", group)
    for string in group:
        if string.startswith("#"):
            group.remove(string)

    return group

catagories = multi_key_dict(catagories)
# use get_key_from_listval to find cata number

probs = open("Packet/ex_problems.txt")
sols = open("Packet/ex_solutions.txt")

problems = clean_up(probs.read())
solutions = clean_up(sols.read())

for idx, p in enumerate(problems):
    print str(idx + 1) + "." + p
print "-------------------------------------------------------------------------------------------------------------"
for idx, s in enumerate(solutions):
    print str(idx + 1) + "." + s

probs.close()
sols.close()
