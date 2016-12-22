import numpy as np
import csv
from sklearn.cluster import KMeans

with open('/Users/rachelren/Documents/EECS6893/kmeans_input.txt', 'rb') as f:
    reader = csv.reader(f)
    data = list(reader)

with open('/Users/rachelren/Documents/EECS6893/profiles_new.csv', 'rb') as f:
    reader = csv.reader(f)
    raw_data = list(reader)

header = raw_data[0]
raw_data = raw_data[1:]

kmeans = KMeans(n_clusters=15, random_state=0).fit_predict(data)

count_male = [0] * 15
count_female = [0] * 15
newHeader = ['cluster'] + header
processedData = [newHeader]

headerCat = ['cluster', 'age', 'drink', 'education', 'height', 'target sex', 'zodiac', 'smoke']
catData = [headerCat]

#first process male
for idx in range(0, len(kmeans)):
    label = kmeans[idx]
    sex = raw_data[idx][5]
    if sex == 'm':
        if (label <= 2 and count_male[label] < 78) or (label >= 3 and count_male[label] < 79):
            processedData.append([label] + raw_data[idx])
            catData.append([label] + data[idx])
            count_male[kmeans[idx]] += 1

print count_male

#next process female
for idx in range(0, len(kmeans)):
    label = kmeans[idx]
    sex = raw_data[idx][5]
    if sex == 'f':
        if (label <= 2 and count_female[label] < 60) or (label >= 3 and count_female[label] < 61):
            processedData.append([label] + raw_data[idx])
            catData.append([label] + data[idx])
            count_female[kmeans[idx]] += 1

print count_female

with open('/Users/rachelren/Documents/EECS6893/processed_kmeans.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(processedData)


with open('/Users/rachelren/Documents/EECS6893/kmeans_categorical_result.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(catData)

f.close()