import csv
from sets import Set

'''
Step 3.2:
This file will modify the text data to categorical data for each entry.
'''



def educationCategory(data):
    '''
    This function will map every possible education to four category:
    0. lower than high school
    1. high school
    2. space camp
    3. bachelor
    4. graduate or above
    input: a list of possible entries for education
    output: a python dictionary that maps possible entry to its category
    '''
    map = {}
    for entry in data:
        if 'high school' in entry:
            if 'graduated' in entry:
                map[entry] = 1
            else:
                map[entry] = 0
        elif 'camp' in entry:
            map[entry] = 2
        elif 'college' in entry or 'university' in entry:
            map[entry] = 3
        else:
            map[entry] = 4

    return map



def processRow(row, map):
    '''
    This function will process each entry in a row based on the category we have already
    extracted from data (stored in map)
    input:
    row = a list of string
    map = a list of list
    output:
    newRow = new list of processed data
    '''
    newRow = []
    newRow.append(processAge(row[0]))
    newRow.append(processDrink(row[1], map[1]))
    newRow.append(processEducation(row[2], map[2]))
    newRow.append(processHeight(row[3], row[6], map[3]))
    newRow.append(processTargetSex(row[4], row[5]))
    newRow.append(processZodiac(row[6]))
    newRow.append(processSmoke(row[7], map[7]))

    return newRow

def processAge(entry):
    '''
    This function will process age
    0: below 20
    1: 20 - 23
    2: 23 - 25
    3: 25 - 27
    4: 27 - 29
    5: 29 - 31
    6: 31 - 33
    7: 33 - 36
    8: 36 - 40
    9: 40 - 45
    10: 45 - 50
    11: 50 - 55
    12: Above 55
    '''
    entry = int(entry)
    if entry < 20:
        return 0
    elif 20 <= entry < 23:
        return 1
    elif 23 <= entry < 25:
        return 2
    elif 25 <= entry < 27:
        return 3
    elif 27 <= entry < 29:
        return 4
    elif 29 <= entry < 31:
        return 5
    elif 31 <= entry < 33:
        return 6
    elif 33 <= entry < 36:
        return 7
    elif 36 <= entry < 40:
        return 8
    elif 40 <= entry < 45:
        return 9
    elif 45 <= entry < 50:
        return 10
    elif 50 <= entry < 55:
        return 11
    else:
        return 12

def processDrink(entry, cat):
    '''
    This function will process drink
    0: 'desperately'
    1: 'often'
    2: 'socially'
    3: 'very often'
    4: 'not at all'
    5: 'rarely'
    input: entry is a string and cat is a list of category
    output: processed string of drinks
    '''
    return cat.index(entry)

def processEducation(entry, cat):
    '''
    This function will process education
    input: entry is a string and cat is a map of category to its categorical value
    output: processed string of education
    '''
    return cat[entry]

def processHeight(entry, sex, cat):
    '''
    This function will process height
    Female:
    0: below 40
    1: 40 - 50
    2: 50 - 55
    3: 55 - 60
    4: 60 - 65
    5: 65 - 70
    6: higher than 70

    Male:
    0: below 50
    1: 50 - 60
    2: 60 - 65
    3: 65 - 70
    4: 70 - 75
    5: 75 - 80
    6: higher than 80

    input:
    entry is a string
    sex is a string
    cat is a map of category to its categorical value
    output: processed string of education
    '''
    entry = int(entry)
    if sex == 'f':
        if entry < 40:
            return 0
        elif 40 <= entry < 50:
            return 1
        elif 50 <= entry < 55:
            return 2
        elif 55 <= entry < 60:
            return 3
        elif 60 <= entry < 65:
            return 4
        elif 65 <= entry < 70:
            return 5
        else:
            return 6
    else:
        if entry < 50:
            return 0
        elif 50 <= entry < 60:
            return 1
        elif 60 <= entry < 65:
            return 2
        elif 65 <= entry < 70:
            return 3
        elif 70 <= entry < 75:
            return 4
        elif 75 <= entry < 80:
            return 5
        else:
            return 6

def processTargetSex(orientation, sex):
    '''
    This function will process target sex
    target sex:
    0: female
    1: male
    2: both
    We will take consideration of sexual orientation when deciding
    target sex
    input:
    orientation is a string indicating the sexual orientation
    sex is a string indicating the gender
    output:
    processed category
    '''
    if orientation == 'bisexual':
        return 2
    elif orientation == 'straight':
        if sex == 'm':
            return 0
        else:
            return 1
    elif orientation == 'gay':
        if sex == 'm':
            return 1
        else:
            return 0

def processZodiac(entry):
    '''
    This function will process zodiac
    0: aries
    1: taurus
    2: gemini
    3: cancer
    4: leo
    5: virgo
    6: libra
    7: scorpio
    8: sagittarius
    9: capricorn
    10: aquarius
    11: pisces
    input: the string indicate zodiac
    output: corresponding category
    '''
    if 'aries' in entry:
        return 0
    elif 'taurus' in entry:
        return 1
    elif 'gemini' in entry:
        return 2
    elif 'cancer' in entry:
        return 3
    elif 'leo' in entry:
        return 4
    elif 'virgo' in entry:
        return 5
    elif 'libra' in entry:
        return 6
    elif 'scorpio' in entry:
        return 7
    elif 'sagittarius' in entry:
        return 8
    elif 'capricorn' in entry:
        return 9
    elif 'aquarius' in entry:
        return 10
    elif 'pisces' in entry:
        return 11

def processSmoke(entry, map):
    '''
    This function will process smoke
    0: 'yes'
    1: 'sometimes'
    2: 'trying to quit'
    3: 'when drinking'
    4: 'no'
    input:
    entry - a string indicates smoking history
    map - category
    output:
    processed category
    '''
    return map.index(entry)

if __name__ == "__main__":
    print 'reading data...'
    data = []
    header = []
    with open('/Users/rachelren/Documents/EECS6893/profiles_new.csv', 'rb') as f:
        reader = csv.reader(f)
        raw_data = list(reader)

    data = raw_data[1:]
    header = raw_data[0]

    map = []
    for idx in xrange(0, len(header)):
        map.append(Set())

    print "find category"
    for rowN in xrange(0, len(data)):
        for colN in xrange(0, len(data[rowN])):
            map[colN].add(data[rowN][colN])


    for idx in xrange(0, len(header)):
        print "category "+header[idx]
        map[idx] = list(map[idx])
        print map[idx]

    #process education
    map[2] = educationCategory(map[2])



    print "start to process data..."
    newData = []
    for rowN in xrange(0, len(data)):
        newData.append(processRow(data[rowN], map))

    print "write output to file"
    with open('/Users/rachelren/Documents/EECS6893/kmeans_input.txt', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(newData)

    f.close()

