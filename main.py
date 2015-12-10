from __future__ import print_function
import findspark 
findspark.init()
from pyspark import SparkContext
from operator import add
from numpy import array
from pyspark.mllib.clustering import LDA, LDAModel
from pyspark.mllib.linalg import Vectors
from stop_words import get_stop_words
from gensim import corpora, models
import sys
import textmining
import numpy as np
import lda
import lda.datasets

#filters out unwanted words and returns a list of words to use
def clean(list):
    print (list)
    # create English stop words list
    en_stop = get_stop_words('en')
    toret = []
    for word in list.split():
        token = word.lower().decode("ascii", "ignore")
        # remove stop words from tokens
        if not token in en_stop and token.isalpha() and not token.isdigit() and not token.isspace():
            toret.append(token)

    return toret

if __name__ == "__main__":

    sc = SparkContext()
    # Open / read file and load and parse data into sections
    delimiter = "\n\n"
    # contents = open("dsmiv.txt").read()
    contents = open("ShortDiagTest.txt").read()
    #DSM4 = sc.parallelize(contents.split(delimiter), 100)
    DSM4 = sc.parallelize(contents.split(delimiter), 100)
    print (DSM4.take(3))
    #the rdd of words to use
    cleaned = DSM4.flatMap(lambda w: clean(w))

    #print(cleaned.take(5))

                                                          
    sc.stop()
    


