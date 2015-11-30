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

    delimiter = ' '
    #delimiter = "This page intentionally left blank\n\n"
    contents = open("testfile.txt").read()
    DSM4 = sc.parallelize(contents.split(delimiter))
    # open / read the file

    # split words apart to be filtered
    split = DSM4.flatMap(lambda x: x.split("#"))
    output = split.collect()
    print(split.take(5))

    #for (word) in output:
    #    print("%s \n \n" % (word))
                                                          
    sc.stop()
