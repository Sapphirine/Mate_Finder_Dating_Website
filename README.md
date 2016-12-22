# MateFinder - The Next Generation of Dating Recommender
This is the next generation of dating recommendation system developed by Jinyang Yu(jy2803), Lyujia Zhang(lz2467) and Chuqiao Ren(cr2826) at Columbia University in the city of New York (GroupID: 201612-62)     
You can find the report in this repo called MateFinder-TheNextGenerationofDatingRecommendationSystem.pdf

## How to access our website?
We have hosted our website on AWS Elestic Beanstalk -> [http://matefinder-env.xmx2nui3gd.us-west-2.elasticbeanstalk.com/MateFinder](http://matefinder-env.xmx2nui3gd.us-west-2.elasticbeanstalk.com/MateFinder)      
If you want to run locally, you must first install all the dependencies following the guide below. And then you can find detail instructions in section __how to run locally__.

## Install Dependencies
Here we assume that you have already installed python (ver 2 or ver 3).  
You want to first install pip through this stand-alone pip installer through python -> [link](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py)  
Then you are able to install all dependencies through pip:
+ django: pip install Django
+ numpy, scipy: pip install numpy/scipy
+ scikit-learn: pip install -U scikit-learn
+ MySQL python: pip install MySQL-python
+ Microsoft Cognitive API (for face recognition): pip install cognitive_face
+ Cloudinary API (for image storage): pip install cloudinary

In case you have Anaconda, you want to resolve the python path. I have encountered a lot of problems working with both Anaconda python and Django, but I finally resolved all problems. Please contact me through my Columbia email if you encountered any problems. I might be able to help! By the way, here is a great [article](http://www.alirazabhayani.com/2014/12/psycopg2-macos-x-library-not-loaded.html) for one of the problem I encountered millions of times. 

## How to run locally?
You want to clone this file to your laptop or desktop.  
Then open a terminal and cd to this folder.  
Then run the following command:
```
python manage.py runserver
```
You will get a lot of messages. And at the very last lines, you got a message something like:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Copy and paste the server address (might not be identical in your case) to the browser, and then you will find the index page.

## Ideas behind this website
The figure below demonstrate the process for our web application. Both processed categorical data as well as the detailed profile data with image url are stored in AWS RDS MySQL database waiting for query. Once the user provides the questionnaire answer and upload a photo, the photo will be stored to Cloudinary and a unique image URL will be returned. This will be used in Microsoft Face API to detect new face. All other information will be stored in the memory, and Python Spark will query the processed categorical data from database and build the kmeans model. The model will then be interpreted by scikit-learn and it will then find the closest cluster for the given user profile information. The resulted cluster information will then be passed to Microsoft Face API. In the Microsoft API, the user’s face will be compared to all faces that belong to this cluster, and we will display the top matches (normally less than 10 recommendation results). We used Python Django to connect database with frontend, and we used HTML5, CSS and JavaScript to design the webpage in order to give the best user-experience. We have uploaded our website to AWS Elastic Beanstalk for public usage.

![technical overview](https://renchuqiao.github.io/2016/12/22/project-image/overall_tech.png)

## Screenshot of the running website
The welcome page:
![welcome page](https://renchuqiao.github.io/2016/12/22/project-image/welcome_page.png)
After you hit start, it will transit to the suvery page:
![suvery page](https://renchuqiao.github.io/2016/12/22/project-image/survey_page.png)
After finishing filling out all the informations and uploaded your photo, please hit match and then you will be directed to the following recommendation page. On the recommendation page, you will find the top match based on your profile information and your photo.
![recommendation](https://renchuqiao.github.io/2016/12/22/project-image/recommendation_list.png)
If there is no matches, the following page will be shown:
![no match](https://renchuqiao.github.io/2016/12/22/project-image/cannot_find.png)
