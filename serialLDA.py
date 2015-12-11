""""
Successful Test

Results (for short.txt):

See serialLDAplot.png for plot

('Checkpoint 1: CSV File Created. Seconds:', 0.014208793640136719)
('Checkpoint 2: Matrix Data Created. Seconds:', 0.03895282745361328)
((167,), (11, 167))
('Checkpoint 3: Model Fitted. Seconds:', 30.44348978996277)
Topic 0: presence elementary multiple paragraph relatively intelligence substantially ability
Topic 1: samples developed fall performance difficulties attention ability terms
Topic 2: excessively measured standardized decoding ability terms evaluation reading
Topic 3: reading disorder age deficit oral interferes feature standardized
Topic 4: signs numbers symbols reading written arithmetic understanding linguistic
Topic 5: poor measured remediation evaluation grammatical children functional written
Topic 6: writing activities disorders oral difficulties ability terms evaluation
Topic 7: skills objects may operations including attention remembering daily
Topic 8: comprehension activities substantially individuals also speed distortions terms
Topic 9: spelling disorder expression known particularly except establish written
Topic 10: child organization copy texts written ability terms evaluation
Topic 11: written handwriting impairment generally absence early evidenced extent
Topic 12: write well combination especially problems errors reading correctly
Topic 13: medical achievement oral decoding terms evaluation reading correctly
Topic 14: present measured mathematics difficulties education neurological chronological general
Topic 15: mathematical ability calculation naming add impaired decoding numerical
Topic 16: criterion sensory achievement characterized require tests expected intelligence
Topic 17: condition assessment tasks dictation asked case schoolwork oral
Topic 18: less diagnosis observing area oral written terms evaluation
Topic 19: significantly oral grades sentences necessary within young individually
('Checkpoint 4: About to Create Plot. Seconds:', 30.445133924484253)

""""
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

import textmining
import numpy as np
from stop_words import get_stop_words
import matplotlib.pyplot as plt
import lda
import time

start_time = time.time()
word_list = []
num_list = []
wordcnt = []
docs = []
# create English stop words list
en_stop = get_stop_words('en')
texts = []
# Initialize class to create term-document matrix
tdm = textmining.TermDocumentMatrix()
# Add the documents

with open('short.txt','r') as f:
    for line in f:
        raw = line.lower()
        tokens = raw.split()
        for word in tokens:
            token = word#.decode("ascii", "ignore")
            #print token, type(token)
            # remove stop words from tokens
            if not token in en_stop and token.isalpha():
                texts.append(token)
        doc = ' '.join(texts)
        tdm.add_doc(doc)

tdm.write_csv('matrix1.csv', cutoff=1)
chk = time.time()
cp1 = chk - start_time
print ("Checkpoint 1: CSV File Created. Seconds:", cp1 )
"""
# Instead of writing out the matrix you can also access its rows directly.
# Let's print them to the screen.
for row in tdm.rows(cutoff=1):
    print row
"""
# reading in all data into a NumPy array
all_data = np.genfromtxt("matrix1.csv", delimiter=",", dtype = None)
                      
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

model = lda.LDA(n_topics=20, n_iter=1500, random_state=1) #1500
model.fit(X)

chk = time.time()
cp3 = chk - cp2
print ("Checkpoint 3: Model Fitted. Seconds:", cp3 )

topic_word = model.topic_word_
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
""" 
doc_topic = model.doc_topic_
for i in range(10):
     print('Topic {}: {}'.format(titles[i], doc_topic[i].argmax()))
"""

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