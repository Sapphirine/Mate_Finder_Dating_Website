import matplotlib.pyplot as plt
import csv
import numpy as np
import seaborn as sns

'''
Step 3.1:
This file will analyze raw data for partition purpose.
'''

if __name__ == "__main__":

    sns.set(color_codes=True)

    print 'reading data...'
    data = []
    header = []
    with open('/Users/rachelren/Documents/EECS6893/profiles_new.csv', 'rb') as f:
        reader = csv.reader(f)
        raw_data = list(reader)

    data = raw_data[1:]
    header = raw_data[0]

    age = []

    for rowN in xrange(0, len(data)):
        age.append(int(data[rowN][0]))

    plt.title("Age Distributageion")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    sns.distplot(np.array(age))
    sns.plt.show()


    height_female = []
    height_male = []

    for rowN in xrange(0, len(data)):
        height = int(data[rowN][3])
        if data[rowN][5] == 'm':
            height_male.append(height)
        else:
            height_female.append(height)

    plt.clf()
    plt.title("Height for each gender")
    plt.xlabel("Height")
    plt.ylabel("Frequency")
    bins = np.linspace(40, 100, 50)
    sns.distplot(np.array(height_female), bins,  label='female')
    sns.distplot(np.array(height_male), bins,  label='male')
    plt.legend(loc='upper right')
    sns.plt.show()