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
#print (words.shape, matrix.shape)
                      
# use matplotlib style sheet
try:
    plt.style.use('ggplot')
except:
    # version of matplotlib might not be recent
    pass

X = matrix.astype(np.int64)
vocab = words
#titles = lda.datasets.load_reuters_titles()

model = lda.LDA(n_topics=20, n_iter=100, random_state=1) #1500
model.fit(X)
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

f, ax= plt.subplots(5, 1, figsize=(8, 6), sharex=True)
for i, k in enumerate([0, 5, 9, 14, 19]):
    ax[i].stem(topic_word[k,:], linefmt='b-',
               markerfmt='bo', basefmt='w-')
    ax[i].set_xlim(-50,4350)
    ax[i].set_ylim(0, 0.08)
    ax[i].set_ylabel("Prob")
    ax[i].set_title("topic {}".format(k))

ax[4].set_xlabel("word")

plt.tight_layout()
plt.show()                     

    



     
