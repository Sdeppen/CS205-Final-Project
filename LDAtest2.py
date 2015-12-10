# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 18:52:18 2015

@author: sdeppen
"""

import numpy as np
import lda
import lda.datasets

X = lda.datasets.load_reuters()
vocab = lda.datasets.load_reuters_vocab()
titles = lda.datasets.load_reuters_titles()
print X.shape
print X.sum()
model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)
topic_word = model.topic_word_
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
    
doc_topic = model.doc_topic_
for i in range(10):
     print('Topic {}: {}'.format(titles[i], doc_topic[i].argmax()))