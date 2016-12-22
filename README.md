# MateFinder - The Next Generation of Dating Recommender
This is the next generation of dating recommendation system developed by Jinyang Yu(jy2803), Lyujia Zhang(lz2467) and Chuqiao Ren(cr2826) at Columbia University in the city of New York

## How to access our website?
We have hosted our website on AWS Elesticbeanstalk.  
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
