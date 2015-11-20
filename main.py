import findspark 
findspark.init()
from pyspark import SparkContext
from pyspark.mllib.clustering import LDA, LDAModel
sc = SparkContext()

# Load and parse data into sections
DSM4 = sc.textFile("dsm-iv-2 edits.txt")

#split words apart to be filtered
cleanup = DSM4.map(lambda w: w.split("This page intentionally left blank"))

