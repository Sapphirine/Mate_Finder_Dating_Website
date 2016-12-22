import csv

'''
Step 1:
This script will extract features we would like to cover in the kmeans.
It includes: age, drinks, education, height, location, sexual orientation, sex, zodiac and smoke
'''

if __name__ == "__main__":

    print 'reading data...'
    data = []
    header = []
    with open('/Users/rachelren/Documents/EECS6893/profiles.csv', 'rb') as f:
        reader = csv.reader(f)
        raw_data = list(reader)

    data = raw_data[1:]
    header = raw_data[0]

    newData = [['age','drinks','education','height','sexual orientation','sex','zodiac','smoke']]

    index = [1,4,6,18,24,27,28,29]

    index_map = {}

    for idx in index:
        index_map[idx] = {}

    for rowNum in xrange(0, len(data)):
        newRow = []
        for colNum in xrange(0, len(data[rowNum])):
            if colNum in index:
                newRow.append(data[rowNum][colNum])
                index_map[colNum][data[rowNum][colNum]] = 1

        newData.append(newRow)

    print "index map is ..."
    for idx in index:
        print "for category "+header[idx]
        print index_map[idx]

    print "write output to new data"
    with open('/Users/rachelren/Documents/EECS6893/profiles_new.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(newData)

    f.close()



