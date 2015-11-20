from __future__ import print_function
import findspark 
findspark.init()
from pyspark import SparkContext
from pyspark.mllib.clustering import LDA, LDAModel
from operator import add
import sys

if __name__ == "__main__":

    sc = SparkContext()
    # Load and parse data into sections
    delimiter = "This page intentionally left blank\n"
    contents = open("testfile.txt").read()
    DSM4 = sc.parallelize(contents.split(delimiter))
    # open / read the file

    #split words apart to be filtered
    #cleanup = DSM4.map(lambda w: w.split("This page intentionally left blank"))
    counts = DSM4.map(lambda w: w.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    output = counts.collect()
    
    for (word, count) in output:
        print("%s: %i" % (word, count)) 
   
    sc.stop()