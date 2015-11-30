from __future__ import print_function
import findspark 
findspark.init()
from pyspark import SparkContext
from pyspark.mllib.clustering import LDA, LDAModel
from operator import add
#from numpy import array
import sys


if __name__ == "__main__":

    sc = SparkContext()
    # Load and parse data into sections
    delimiter = "This page intentionally left blank #"
    # contents = open("dsm-iv-2edits.txt").read()
    contents = open("testfile.txt").read()
    DSM4 = sc.parallelize(contents.split("This page intentionally left blank #"))
    # open / read the file

    # split words apart to be filtered
    split = DSM4.flatMap(lambda x: x.split('#'))
    output = split.collect()

    # parsedData = DSM4.flatMap(lambda section:  section.split(delimiter))
    
    print(split.take(1))

    #for (section) in output:
    #    print("%s" % (section))
                                                          
    sc.stop()
