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

    #split words apart to be filtered
    cleanup = DSM4.flatMap(lambda w: w.split("This page intentionally left blank")) #.map(lambda x: (x, 1)).reduceByKey(add)
    output = cleanup.collect()

    for (word) in output:
        print("%s: END OF SECTION" % (word)) 
 
    #counts = DSM4.flatMap(lambda x: x.split(' ')).map(lambda x: (x, 1)).reduceByKey(add)
    #output = counts.collect()
    
   # for (word, count) in output:
   #     print("%s: %i" % (word, count))

  
    sc.stop()
