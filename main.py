from __future__ import print_function
import findspark 
findspark.init()
from pyspark import SparkContext
from operator import add
from numpy import array
from pyspark.mllib.clustering import LDA, LDAModel
from pyspark.mllib.linalg import Vectors
import sys


if __name__ == "__main__":

    sc = SparkContext()
    # Open / read file and load and parse data into sections
    delimiter = "This page intentionally left blank #"
    # contents = open("dsmiv.txt").read()
    contents = open("testfile.txt").read()
    DSM4 = sc.parallelize(contents.split(delimiter))

    # split words apart to be filtered
    split = DSM4.flatMap(lambda x: x.split(delimiter)).map(lambda y: (y, 1)).reduceByKey(add)
    #output = split.collect()

   # word2vec = Word2Vec()
   # model = word2vec.fit(split)

    
    print(split.take(1))

    #for (section) in output:
    #    print("%s" % (section))
                                                          
    sc.stop()
