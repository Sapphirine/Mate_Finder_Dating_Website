from numpy import array
from math import sqrt
import csv

from pyspark.mllib.clustering import KMeans, KMeansModel
from pyspark import SparkConf, SparkContext

# Evaluate clustering by computing Within Set Sum of Squared Errors
def error(point):
    center = clusters.centers[clusters.predict(point)]
    return sqrt(sum([x**2 for x in (point - center)]))

conf = (SparkConf()
         .setMaster("local")
         .setAppName("Kmeans")
         .set("spark.executor.memory", "3g"))
sc = SparkContext(conf = conf)
# Load and parse the data
data = sc.textFile("/Users/rachelren/Documents/EECS6893/kmeans_input.txt")
parsedData = data.map(lambda line: array([float(x) for x in line.split(',')]))

# Build the model (cluster the data)
error_array = []
for k in xrange(1, 50):
    clusters = KMeans.train(parsedData, k, maxIterations=100,
                        runs=10, initializationMode="random")

    WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)
    print("Within Set Sum of Squared Error = " + str(WSSSE))
    error_array.append(WSSSE)

print error_array

#Write error to output
with open('/Users/rachelren/Documents/EECS6893/kmeans_error.txt', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(error_array)

f.close()

# Save and load model
# clusters.save(sc, "target/org/apache/spark/PythonKMeansExample/KMeansModel")
    # sameModel = KMeansModel.load(sc, "target/org/apache/spark/PythonKMeansExample/KMeansModel")