from django.shortcuts import render

from .models import kmeans,origin

from django.http import HttpResponse

from sklearn.cluster import KMeans
import numpy as np

import cognitive_face as CF
import httplib, urllib, base64
import json
import os

import cloudinary
import cloudinary.uploader
import cloudinary.api


# Create your views here.
def index(request):
    origin_list = origin.objects.all()
    context = {'origin_list': origin_list}
    return render(request, 'MateFinder/index.html', context)

def submit(request):
    age = request.POST['age']
    zodiac = request.POST['zodiac']
    drink = request.POST['drinks']
    education = request.POST['education']
    height = request.POST['height']
    orientation = request.POST['orientation']
    sex = request.POST['gender']
    smoke = request.POST['smoke']
    image_uploaded = request.FILES['photo']


    #Prepare data
    processedData = prepareData([age, zodiac, drink, education,height,orientation,sex,smoke])

    #Run KMeans
    name = ['k_age', 'k_drink', 'k_education', 'k_height', 'k_target_sex', 'k_zodiac', 'k_smoke']
    matrix = []
    for n in name:
        matrix.append(getData(n))

    matrix = np.matrix(matrix)
    matrix = matrix.transpose()
    model = KMeans(n_clusters=15, random_state=0).fit(matrix)
    cluster = model.predict([processedData])[0]

    #Prepare image
    # recommend_list = origin.objects.get(cluster__exact=cluster)
    #
    # message = ''
    # for item in recommend_list.image_url:
    #     message += '%r ' % item

    #========Cloudinary code============
    cloudinary.config(
        cloud_name="chuqiaoren",
        api_key="715198541149411",
        api_secret="FA8Rga8-qX9rgYx4ZHLCXe1Cdjw"
    )

    image_url = str(cloudinary.uploader.upload(image_uploaded)['secure_url'])

    #============================================
    #===Following is the Microsoft Image code====
    #============================================
    # Subscription Key
    KEY = 'd0a3295000d74bae9eca97f2b365837e'  # Replace with a valid Subscription Key here.
    CF.Key.set(KEY)
    # set headers for all HTTP communications
    headers = {
        # Request headers
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': KEY,
    }

    # validate function: check what information WITHIN a FACELIST
    body_check2 = {

    }
    params_check2 = urllib.urlencode({
        "faceListId": 'cluster-'+str(cluster)
    })
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("GET", "/face/v1.0/facelists/{faceListId}?%s" % params_check2, str(body_check2), headers)
        response = conn.getresponse()
        data_check2 = response.read()
        print(data_check2)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    #Detect a new face
    params_detect = urllib.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',

    })
    body_detect = {
        "url": image_url
    }
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/face/v1.0/detect?%s" % params_detect, str(body_detect), headers)
        response = conn.getresponse()
        data_detect = response.read()
        a = json.loads(data_detect.decode('utf-8'))
        faceId = a[0]['faceId']
        print(faceId)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    #recognize new face
    params_similar = urllib.urlencode({
    })
    body_similar = {
        "faceId": str(faceId),
        "faceListId": 'cluster-'+str(cluster),
        "maxNumOfCandidatesReturned": 10,
        "mode": "matchFace"
    }
    try:
        conn = httplib.HTTPSConnection('api.projectoxford.ai')
        conn.request("POST", "/face/v1.0/findsimilars?%s" % params_similar, str(body_similar), headers)
        response = conn.getresponse()
        data_similar = response.read()
        print(data_similar)
        conn.close()
    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

    num_faces = len(json.loads(data_similar.decode('utf-8')))
    returnedID_list = []
    for i in range(0, num_faces):
        returnedID_list.append(str(json.loads(data_similar.decode('utf-8'))[i]['persistedFaceId']))


    facelistcontent = json.loads(data_check2.decode('utf-8'))['persistedFaces']

    returnedURL_list = []
    for i in facelistcontent:
        if i['persistedFaceId'] in returnedID_list:
            returnedURL = i['userData']
            returnedURL_list.append(returnedURL)

    #Retrieve Data from db
    objects = []
    for i in returnedURL_list:
        object = origin.objects.get(image_url__exact=i)
        object.zodiac = object.zodiac.split()[0]
        if str(orientation) == 'Heterosexual':
            if str(object.sex) != str(sex)[0]:
                objects.append(object)
        elif str(orientation) == 'Homosexual':
            if str(object.sex) == str(sex)[0]:
                objects.append(object)
        else:
            objects.append(object)


    #Present Recommendation
    context = {'objects': objects}

    return render(request, 'MateFinder/submit.html', context)


def getData(name):
    result = []
    for item in kmeans.objects.values(name):
        result.append(int(item[name]))
    return result

#=====================================================
#=============Data Preparation Code===================
#=====================================================
def prepareData(input):
    result = []
    result.append(processAge(input[0]))
    result.append(processZodiac(input[1]))
    result.append(processDrink(input[2]))
    result.append(processEducation(input[3]))
    result.append(processHeight(input[4], input[6]))
    result.append(processTargetSex(input[5], input[6]))
    result.append(processSmoke(input[7]))

    return result

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
    if 'Aries' in entry:
        return 0
    elif 'Taurus' in entry:
        return 1
    elif 'Gemini' in entry:
        return 2
    elif 'Cancer' in entry:
        return 3
    elif 'Leo' in entry:
        return 4
    elif 'Virgo' in entry:
        return 5
    elif 'Libra' in entry:
        return 6
    elif 'Scorpio' in entry:
        return 7
    elif 'Sagittarius' in entry:
        return 8
    elif 'Capricorn' in entry:
        return 9
    elif 'Aquarius' in entry:
        return 10
    elif 'Pisces' in entry:
        return 11

def processHeight(entry, sex):
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
    output: processed string of education
    '''
    if '-' in entry:
        entry = int(entry[0:2])
    else:
        if '40' in entry:
            entry = 39
        else:
            entry = 100


    if sex == 'female':
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
    if orientation == 'Bisexual':
        return 2
    elif orientation == 'Heterosexual':
        if sex == 'male':
            return 0
        else:
            return 1
    elif orientation == 'Homosexual':
        if sex == 'male':
            return 1
        else:
            return 0

def processEducation(entry):
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
    if 'Lower than High School' == entry:
        return 0
    elif 'High School' == entry:
        return 1
    elif 'Space Camp' == entry:
        return 2
    elif 'Bachelor' == entry:
        return 3
    elif 'Master and Above' == entry:
        return 4
    else:
        raise KeyError()

def processDrink(entry):
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
    if 'Desperately' == entry:
        return 0
    elif 'Often' == entry:
        return 1
    elif 'Socially' == entry:
        return 2
    elif 'Very Often' == entry:
        return 3
    elif 'Not at all' == entry:
        return 4
    elif 'Rarely' == entry:
        return 5
    else:
        raise KeyError()

def processSmoke(entry):
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
    if 'Yes' == entry:
        return 0
    elif 'Somtimes' == entry:
        return 1
    elif 'Trying to quit' == entry:
        return 2
    elif 'When drinking' == entry:
        return 3
    elif 'No' == entry:
        return 4
    else:
        raise KeyError()