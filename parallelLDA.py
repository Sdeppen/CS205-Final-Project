"""
SUCCESSFUL

RESULTS (for short.txt):

See parallelLDAplot.png for plot

Topic 0: written expression poor excessively necessary child multiple may
Topic 1: measured daily disturbance individually generally called copy except
Topic 2: skills given associated written functional samples assessment remediation
Topic 3: tests achievement medical administered neurological clustering significantly activities
Topic 4: mathematical standardized chronological academic may observing problems impaired
Topic 5: criterion sensory require essential errors coded activities terms
Topic 6: ability mathematics axis signs within calculation attention intelligence
Topic 7: numbers objects sequences following decoding evaluation reading correctly
Topic 8: symbols individually multiplication understanding linguistic operational groups reasoning
Topic 9: terms numerical oral written ability evaluation reading correctly
Topic 10: disorders write young texts known spontaneously well dictation
Topic 11: age condition substantially education present interferes expected significantly
Topic 12: writing spelling standardized impairment criterion schoolwork compared grades
Topic 13: falls appropriate comprehension including add different tables omissions
Topic 14: iii excess oral combination chronological neurological difficulties evaluation
Topic 15: usually present feature intelligence operations accuracy occur case
Topic 16: reading disorder deficit difficulties living general characterized correctly
Topic 17: presence developed area especially relatively general errors evaluation
Topic 18: paragraph grammatical absence compose attention terms evaluation reading
Topic 19: expected handwriting less sentences comparison fall writing test

RESULTS (for ShortDiagText.txt)


See parallelLDAplotMed.png for plot

Topic 0: disorder psychotic schizophrenia delusional symptoms delusions diagnosis type
Topic 1: disorders disorder mood intoxication anxiety symptoms diagnosis withdrawal
Topic 2: symptoms least period months criteria duration mood full
Topic 3: sleep may individuals episodes individual often insomnia also
Topic 4: panic disorder anxiety social phobia attacks fear specific
Topic 5: may criterion often children activities person usually will
Topic 6: disorder sexual symptoms conversion dysfunction symptom complaints somatization
Topic 7: may disease findings laboratory associated include due abnormalities
Topic 8: features specifiers see specifier pattern psychotic used remission
Topic 9: may individuals criterion others often disorder behavior individual
Topic 10: criterion social functioning impairment disorder occupational significant essential
Topic 11: features specific age may culture gender motor activity
Topic 12: may language hallucinations dementia memory individual disturbances speech
Topic 13: disorder disorders associated stress personality mental may features
Topic 14: may onset individuals can age course cases years
Topic 15: medical general condition disorder due direct physiological symptoms
Topic 16: use withdrawal dependence intoxication substance sedative hypnotic substances
Topic 17: delusions weight person body obsessions may nervosa compulsions
Topic 18: depressive disorder episode major episodes bipolar manic mood
Topic 19: individuals disorder prevalence common women reported studies among

"""
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 19:50:08 2015

@author: sdeppen

sources used
https://rstudio-pubs-static.s3.amazonaws.com/79360_850b2a69980c4488b1db95987a24867a.html#importing-your-documents
https://pypi.python.org/pypi/lda
http://www.christianpeccei.com/textmining/
http://chrisstrelioff.ws/sandbox/2014/11/13/getting_started_with_latent_dirichlet_allocation_in_python.html

TODO: Fix time measurement issues 
"""

#import __future__ 
#from __future__ import print_function
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
    start_time = time.time()
    tdm = textmining.TermDocumentMatrix()
    sc = SparkContext()
    delimiter = "\n"
    
    # Open / read file and load and parse data into sections
    contents = open("ShortDiagTest.txt").read()
    DSM4 = sc.parallelize(contents.split(delimiter), 100)
    doc = DSM4.map(lambda w: ' '.join(clean(w))).map(lambda h: h if len(h) > 2 else None).collect()
    sc.stop()
    
    # add lines to text-document matrix
    for d in doc:
        if not d == None:
            tdm.add_doc(d)
    tdm.write_csv('matrix3.csv', cutoff=1)

cp1 = time.time() - start_time
print ("Checkpoint 1: CSV File Created. Seconds:", cp1)

# reading in all data into a NumPy array
all_data = np.genfromtxt("matrix3.csv", delimiter=",", dtype = None)
                      
words = all_data[0,:]
matrix = all_data[1:,:]

cp2 = time.time() - cp1
print ("Checkpoint 2: Matrix Data Created. Seconds:", cp2)
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

cp3 = time.time() - cp2
print ("Checkpoint 3: Model Fitted. Seconds:", cp3)

topic_word = model.topic_word_
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))

cp4 = time.time() - cp3
print ("Checkpoint 4: About to Create Plot. Seconds:", cp4)
f, ax= plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([0, 5, 9, 14, 19]):
    ax[i].stem(topic_word[k,:], linefmt='b-',
               markerfmt='bo', basefmt='w-')
    ax[i].set_xlim(-50,4350) 
    ax[i].set_ylim(0, 0.08) #0.08
    ax[i].set_ylabel("Prob")
    ax[i].set_title("topic {}".format(k))

ax[4].set_xlabel("word")

plt.tight_layout()
plt.show()                     