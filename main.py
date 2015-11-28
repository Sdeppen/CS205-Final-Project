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

    DSM4 = sc.textFile("dsm-iv-2edits.txt")

    delimiter = "This page intentionally left blank\n"
    contents = open("testfile.txt").read()
    DSM4 = sc.parallelize(contents.split(delimiter))
    # open / read the file

   # delimiters = "This page intentionally left blank"
    #split words apart to be filtered
    cleanup = DSM4.flatMap(lambda w: w.split("\n"))#"This page intentionally left blank"))
    output = cleanup.collect()

    for (word) in output:
        print("%s \n \n" % (word))
   
   #counts = DSM4.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    #output = counts.collect()
    
   # for (word, count) in output:
   #     print("%s, %i: END OF LINE" % (word, count)) 
  
    sc.stop()
