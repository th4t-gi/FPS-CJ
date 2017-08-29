catagories = {
    "Arts & Aesthetics" : ['public', 'art', 'arts', 'aesthetics', 'design', 'picture', 'drawing'],
    "Basic Needs" : ['poverty', 'food', 'shelter', 'water', 'basic needs'],
    "Business & Commerce" : ['money', 'cash', 'stock', 'business', 'commerce'],
    "Communication" : ['information', 'communication', 'talking', 'phones', 'connection'],
    "Defense" : ['control', 'country', 'national', 'countries'],
    "Economics" : ['economics', 'banking', 'bank', 'credit', 'credit card'],
    "Education" : ['education', 'educating', 'educate', 'school', 'learn', 'teach'],
    "Environment" : ['environment', 'plants', 'trees', 'animals', 'pollution'],
    "Ethics & Religion" : ['moral', 'right and wrong', 'standards', 'belief', 'religion', 'ethics', 'god'],
    "Government & Politics" : ['government', 'politics', 'countries', 'senate', 'law', 'house of representatives'],
    "Law & Justice" : ['law', 'justice', 'court', 'senate', 'judge'],
    "Misc" : ['dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space'],
    "Physical Health" : ['physical health', 'hospital', 'hospitals', 'injury', 'injuries'],
    "Psychological Health" : ['counseling', 'therapy', 'phycological', 'health', 'crazy', 'mind', 'mental health'],
    "Recreation" : ['enjoyment', 'activity', 'pastime', 'relaxation', 'recreation'],
    "Social Relationships" : ['social', 'relationship', 'individuals', 'agreement'],
    "Technology" : ['technology', 'computers', 'algorithms', 'innovations', 'electricity',
        'machinery', 'dna', 'future', '3d printing', 'ai', ' alien', 'space travel', 'space'],
    "Transportation" : ['transportation', 'cars', 'trains', 'airplanes', 'movement', 'vehicle']
}

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

def subject(text):
    if not isinstance(text, list):
        text = text.split()
