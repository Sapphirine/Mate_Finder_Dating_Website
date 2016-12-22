import csv

'''
Step 2:
This file will remove entrys (rows) that has empty fields (cell)
Also, this file will remove entries that has abnormal heights (less than 25)
'''

if __name__ == "__main__":
    print 'reading data...'
    data = []
    header = []
    with open('/Users/rachelren/Documents/EECS6893/profiles_new.csv', 'rb') as f:
        reader = csv.reader(f)
        raw_data = list(reader)

    data = raw_data[1:]
    header = raw_data[0]

    newData = [header]

    num = len(header)

    for rowNum in xrange(0, len(data)):
        newRow = []
        for colNum in xrange(0, len(data[rowNum])):
            if len(data[rowNum][colNum]) > 0:
                newRow.append(data[rowNum][colNum])
        if len(newRow) == num and int(newRow[3]) > 25:
            newData.append(newRow)

    print "write output to new data"
    with open('/Users/rachelren/Documents/EECS6893/profiles_new.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(newData)

    f.close()