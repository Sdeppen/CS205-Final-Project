# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:50:08 2015

@author: sdeppen

sources used
https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html#importing-your-documents
https://pypi.python.org/pypi/lda
http://www.christianpeccei.com/textmining/
http://chrisstrelioff.ws/sandbox/2014/11/13/getting_started_with_latent_dirichlet_allocation_in_python.html


"""
from __future__ import print_function
import findspark 
findspark.init()
from pyspark import SparkContext
from operator import add
import textmining
import numpy as np
from numpy import array
from stop_words import get_stop_words
import sys
import matplotlib.pyplot as plt
import plda
import time

#filters out unwanted words and returns a list of words to use
def clean(list):
    # create English stop words list
    en_stop = get_stop_words('en')
    toret = []
    for word in list.split():
        token = word.lower() #.decode("ascii", "ignore")
        # remove stop words from tokens
        if not token in en_stop and len(token)>2 and token.isalpha() and not token.isdigit() and not token.isspace() and not (token == '') and not (token == '\n'):
            toret.append(token)

    return toret

if __name__ == "__main__":

    # Initialize class to create term-document matrix
    tdm = textmining.TermDocumentMatrix()
    sc = SparkContext()
    delimiter = "\n"
    
    # Open / read file and load and parse data into sections
    contents = open("short.txt").read()
    DSM4 = sc.parallelize(contents.split(delimiter), 100)
    doc = DSM4.map(lambda w: ' '.join(clean(w))).map(lambda h: h if len(h) > 2 else None).collect()
    sc.stop()
    
    # add lines to text-document matrix
    for d in doc:
        if not d == None:
            tdm.add_doc(d)
    tdm.write_csv('matrix2.csv', cutoff=1)

chk = time.time()
cp1 = chk - start_time
print ("Checkpoint 1: CSV File Created. Seconds:", cp1 )

# reading in all data into a NumPy array
all_data = np.genfromtxt("matrix2.csv", delimiter=",", dtype = None)
                      
words = all_data[0,:]
matrix = all_data[1:,:]

chk = time.time()
cp2 = chk - cp1
print ("Checkpoint 2: Matrix Data Created. Seconds:", cp2 )
print (words.shape, matrix.shape)

# use matplotlib style sheet
try:
    plt.style.use('ggplot')
except:
    # version of matplotlib might not be recent
    pass

X = matrix.astype(np.int64)
vocab = words

model = plda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)

chk = time.time()
cp3 = chk - cp2
print ("Checkpoint 3: Model Fitted. Seconds:", cp3 )

topic_word = model.topic_word_
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))

chk = time.time()
cp4 = chk - cp3
print ("Checkpoint 4: About to Create Plot. Seconds:", cp4)
f, ax= plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([0, 5, 9, 14, 19]):
    ax[i].stem(topic_word[k,:], linefmt='b-',
               markerfmt='bo', basefmt='w-')
    ax[i].set_xlim(-50,200) #-50, 4350
    ax[i].set_ylim(0, 0.3) #0.08
    ax[i].set_ylabel("Prob")
    ax[i].set_title("topic {}".format(k))

ax[4].set_xlabel("word")

plt.tight_layout()
plt.show()                     