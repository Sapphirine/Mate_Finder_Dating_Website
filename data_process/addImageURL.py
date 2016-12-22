import csv
import os

rootdir_male = '/Users/rachelren/Documents/renchuqiao.github.io/source/_posts/male'
rootdir_female = '/Users/rachelren/Documents/renchuqiao.github.io/source/_posts/female'

with open('/Users/rachelren/Documents/EECS6893/processed_kmeans.csv', 'rb') as f:
    reader = csv.reader(f)
    raw_data = list(reader)

header = raw_data[0]
raw_data = raw_data[1:]

newHeader = header + ['image_url']
newData = [newHeader]

idx = 0
for subdir, dirs, files in os.walk(rootdir_male):
    for file in files:
        if '.jpg' in str(file):
            newData.append(raw_data[idx])
            newData[idx + 1].append("https://renchuqiao.github.io/2016/12/21/male/"+str(file))
            idx += 1

for subdir, dirs, files in os.walk(rootdir_female):
    for file in files:
        if '.jpg' in str(file):
            newData.append(raw_data[idx])
            newData[idx + 1].append("https://renchuqiao.github.io/2016/12/21/female/" + str(file))
            idx += 1

print "write output to file"
with open('/Users/rachelren/Documents/EECS6893/final_data_with_image_url.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(newData)

f.close()

