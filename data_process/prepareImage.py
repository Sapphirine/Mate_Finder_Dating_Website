import cognitive_face as CF
import httplib, urllib, base64
import json
import os
from time import sleep
import csv


def createFaceList(cluster, data, header):
    # First step: Create a face list first. The face list is stored inside my FACE API account. So rerun the code with same
    # faceListId does not work.
    params_createlist = urllib.urlencode({
        # arbitrary numerical values.
        'faceListId': 'cluster-'+str(cluster)
    })
    body_createlist = {
        # variable name
        "name": "sampleListName"
    }
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("PUT", "/face/v1.0/facelists/{faceListId}?%s" % params_createlist, str(body_createlist), headers)
        response = conn.getresponse()
        data_createlist = response.read()
        print(data_createlist)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    # Second step: Add image to facelist

    for url in data:
        image_url = url

        params_add = urllib.urlencode({
            # Request parameters
            'faceListId': 'cluster-'+str(cluster),
            'userData': image_url
        })
        body_add = {
            "url": image_url
        }
        try:
            conn = httplib.HTTPSConnection('api.projectoxford.ai')
            conn.request("POST", "/face/v1.0/facelists/{faceListId}/persistedFaces?%s" % params_add,
                         str(body_add), headers)
            response = conn.getresponse()
            data_add = response.read()
            print(image_url,str(cluster),data_add)
            conn.close()
        except Exception as e:
            print(e)
        sleep(0.5)
    print 'done'



#Free Key
# KEY = '6cd133180bf94f36b967f04bf8ade1bd'  # Replace with a valid Subscription Key here.
#Subscription Key
KEY = 'd0a3295000d74bae9eca97f2b365837e'
CF.Key.set(KEY)
# set headers for all HTTP communications
headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': KEY,
}



with open('/Users/rachelren/Documents/EECS6893/database/final_data_with_image_url.csv', 'rb') as f:
    reader = csv.reader(f)
    raw_data = list(reader)

data = raw_data[1:]

for cluster in xrange(0, 15):
    cluster_data = []
    for row in data:
        if int(row[0]) == cluster:
            cluster_data.append(row[-1])
    createFaceList(cluster, cluster_data, headers)



