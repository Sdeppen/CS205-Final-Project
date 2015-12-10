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
import lda
from stop_words import get_stop_words

word_list = []
num_list = []
wordcnt = []
counter = 1
docs = []
# create English stop words list
en_stop = get_stop_words('en')
texts = []
# Initialize class to create term-document matrix
tdm = textmining.TermDocumentMatrix()
# Add the documents

with open('ShortDiagTest.txt','r') as f:
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

tdm.write_csv('matrix.csv', cutoff=1)
# Instead of writing out the matrix you can also access its rows directly.
# Let's print them to the screen.
for row in tdm.rows(cutoff=1):
    print row

# reading in all data into a NumPy array
all_data = np.loadtxt(open("matrix.csv","r"),
    delimiter=",",
    skiprows=0,
    dtype=np.float64
    )

        
    



     
        
        
"""
f = []
for i in range(len(wordcnt)):
    if ((wordcnt[i] > 100)): #and (len(word_list[i]) > 4)):
        f.append(word_list[i])
        
tdms = []
for line in f:
    tdm = textmining.TermDocumentMatrix()
    tdm.add_doc(line.strip())
    tdms.append(tdm)

***
for tdm in tdms:
    for row in tdm.rows(cutoff=1):
        print row
***

X = tdms #lda.datasets.load_reuters()
vocab = f# lda.datasets.load_reuters_vocab()            
print f

model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)
topic_word = model.topic_word_
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
"""     
