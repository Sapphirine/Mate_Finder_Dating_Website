import os

rootdir = '/Users/rachelren/Documents/renchuqiao.github.io/source/_posts/female'

idx = 1
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if '.jpg' in str(file):
            print '!['+str(idx)+']('+str(file)+')'
            idx += 1
