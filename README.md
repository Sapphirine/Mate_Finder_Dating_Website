# MateFinder - The Next Generation of Dating Recommender
This is the next generation of dating recommendation system developed by Jinyang Yu(jy2803), Lyujia Zhang(lz2467) and Chuqiao Ren(cr2826) at Columbia University in the city of New York (GroupID: 201612-62)  
Youtube Link of the Demo: https://www.youtube.com/watch?v=s0jdQnAJM_c&feature=youtu.be

## Technical Overview
![technical overview](https://renchuqiao.github.io/2016/12/22/project-image/overall_tech.png)
The figure above demonstrate the process for our web application. Both processed categorical data as well as the detailed profile data with image url are stored in AWS RDS MySQL database waiting for query. Once the user provides the questionnaire answer and upload a photo, the photo will be stored to Cloudinary and a unique image URL will be returned. This will be used in Microsoft Face API to detect new face. All other information will be stored in the memory, and Python Spark will query the processed categorical data from database and build the kmeans model. The model will then be interpreted by scikit-learn and it will then find the closest cluster for the given user profile information. The resulted cluster information will then be passed to Microsoft Face API. In the Microsoft API, the user’s face will be compared to all faces that belong to this cluster, and we will display the top matches (normally less than 10 recommendation results). We used Python Django to connect database with frontend, and we used HTML5, CSS and JavaScript to design the webpage in order to give the best user-experience. We have uploaded our website to AWS Elastic Beanstalk for public usage.

## File Structure
    .
    ├── MateFinder_BigDataAnalytics        # Python Django Files (you want to run locally from this folder)
    ├── docs                               # Documentation files (contains presentation PPT and final report)
    ├── data_process                       # Python files that preprocess profile data and image URL
    ├── LICENSE
    └── README.md
### MateFinder_BigDataAnalytics Folder Structure
    .
    ├── ...
    ├── MateFinder_BigDataAnalytics         # Python Django Files (you want to run locally from this folder)
    │   ├── MateFinder                      # The application folder (all the code is here)
    │   │       ├── view.py                 # Controller connecting frontend and backend and do kmeans and image processing
    │   │       ├── model.py                # Connecting to AWS MySQL database
    │   │       ├── static                  # This folder contains all the CSS and JS files
    │   │       └── templates               # This folder contains HTML templates
    │   ├── MateFinder_BigDataAnalytics     # Main website folder (contains settings and URLs)
    │   └── manager.py                      # python file comes with Django that can manage the project
    └── ...
### Data Process folder
    .
    ├── ...
    ├── data_process                        # Python files that preprocess profile data and image URL
    │   ├── addImageURL.py                  # Append image URL to the csv file
    │   ├── analyzeData.py                  # step3.1: This file will analyze raw data for partition purpose.
    │   ├── generate_photo_markdown.py      # Create a markdown file that will be used in Github I/O
    │   ├── kmeans.py                       # Use `Spark` to do kmeans
    │   ├── kmeansPredict.py                # Use `Spark` to predict new data
    │   ├── plotError.py                    # Plot K vs. error plot
    │   ├── prepareImage.py                 # Add photo to Microsoft Cognitive Server
    │   ├── prepareKmeans.py                # Step 3.2: modify the text data to categorical data for each entry.
    │   ├── preprocess.py                   # Step 1: Extract features we would like to cover in the kmeans.
    │   └── removeEmpty.py                  # Step 2: Remove entrys (rows) that has empty fields (cell) and abnormal heights
    └── ...

## How to access our website?
We have hosted our website on AWS Elestic Beanstalk -> [http://matefinder-env.xmx2nui3gd.us-west-2.elasticbeanstalk.com/MateFinder](http://matefinder-env.xmx2nui3gd.us-west-2.elasticbeanstalk.com/MateFinder)  
Note: If you cannot open this link, this is because we have stopped our server due to high cost. In this case, please refer to our demo or contact us. Or you can see some screenshots at the very bottom of this README file.

If you want to run locally, you must first install all the dependencies following the guide below. And then you can find detail instructions in section __how to run locally__.

## Install Dependencies
Here we assume that you have already installed python (ver 2 or ver 3) and Spark.  
You want to first install pip through this stand-alone pip installer through python -> [link](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py)  
Then you are able to install all dependencies through pip:
+ django: `pip install Django`
+ numpy, scipy: `pip install numpy/scipy`
+ scikit-learn: `pip install -U scikit-learn`
+ MySQL python: `pip install MySQL-python`
+ Microsoft Cognitive API (for face recognition): `pip install cognitive_face`
+ Cloudinary API (for image storage): `pip install cloudinary`
+ Seaborn (to plot pretty figures): `pip install seaborn`

In case you have Anaconda, you want to resolve the python path. I have encountered a lot of problems working with both Anaconda python and Django, but I finally resolved all problems. Please contact me through my Columbia email if you encountered any problems. I might be able to help! By the way, here is a great [article](http://www.alirazabhayani.com/2014/12/psycopg2-macos-x-library-not-loaded.html) for one of the problem I encountered millions of times. 

## How to run locally?
You want to clone this file to your laptop or desktop.  
Then open a terminal and cd to `MateFinder_BigDataAnalytics` folder.  
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

## Screenshot of the running website
The welcome page:
![welcome page](https://renchuqiao.github.io/2016/12/22/project-image/welcome_page.png)
After you hit start, it will transit to the suvery page:
![suvery page](https://renchuqiao.github.io/2016/12/22/project-image/survey_page.png)
After finishing filling out all the informations and uploaded your photo, please hit match and then you will be directed to the following recommendation page. On the recommendation page, you will find the top match based on your profile information and your photo.
![recommendation](https://renchuqiao.github.io/2016/12/22/project-image/recommendation_list.png)
If there is no matches, the following page will be shown:
![no match](https://renchuqiao.github.io/2016/12/22/project-image/cannot_find.png)

## Visualization of the data
We have plot the age distribution, height distribution in order to understand the data.
![age](https://renchuqiao.github.io/2016/12/22/project-image/age.png)
![height](https://renchuqiao.github.io/2016/12/22/project-image/height.png)
We used pySpark to analyze our data and plot the K vs. Error in order to determine the number of clusters:
![kmeans_error](https://renchuqiao.github.io/2016/12/22/project-image/kmeans_error.png)
Based on Elbow rule, we chose K = 15 as our final size of clusters.

## Face Recognization Result
![face](https://renchuqiao.github.io/2016/12/22/project-image/correct_detection_lz2467.png)  
The image above shows the face detected by the Microsoft Face API.

## Issues with Microsoft Face API
There are several exceptions when uploading all the images to the Microsoft API. For example, the following two faces returned error messages saying that the API detected __more than 1 face__.
![more_than_one_face_1](https://renchuqiao.github.io/2016/12/22/project-image/error_detection_1.png)
![more_than_one_face_2](https://renchuqiao.github.io/2016/12/22/project-image/error_detection_2.png)
Also, the API __cannot find any face__ for the following image:  
![no_face](https://renchuqiao.github.io/2016/12/21/female/jp3495.jpg)   
These are the only exceptions when using this API. In general, this is a quite powerful API.

## Acknowledgement
We would like to thank Prof. Lin for the fantastic lecture. We would also like to thank all the teaching assistants that helped us with our final project, especially on using PySpark.

## DataSet
You can find all the photo here:   
Chicago Face Dataset: http://faculty.chicagobooth.edu/bernd.wittenbrink/cfd/index.html       
Big Data Anlytics Student Profile Pictures: http://www.ee.columbia.edu/~cylin/course/bigdata/images/      
OkCupid Profile data: https://github.com/rudeboybert/JSE_OkCupid    
   
## Reference:
Online Dating Recommendations: Matching Markets and Learning Preferences  
 




