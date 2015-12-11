# CS205-Final-Project
Final Project manipulating DSM-IV for data analysis

Authors: Sylvia Deppen and Ting Zhou
Supervisor: Dr. Thouis Jones
Website: http://sdeppen.wix.com/dsm-project

The goal of our project was to use LDA and Word2Vec to derive links within the Diagnostic and Statistical Manual of Mental Disorders, 4th Edition.

The relevant files include:
dsm-iv-unedited.txt - original enedited, long DSM
dsm-iv-diagnosis.txt - medium-length DSM
short.txt - a very short test file
matrix1.csv - document-term matrix
parallelLDA.py - parallelized LDA
plda.py - functions for parallelLDA.py
serialLDA.py - serial LDA
serialLDAplot.png - plot resulting from LDA
word2vec.py - word2vec training
wordvis.py - word2vec visualization program
word2vec_vis.png - word2vec visualization plot
tsne.py - Created by Laurens van der Maaten on 20-12-08, t-SNE visualization program
vectors.txt - trained vectors: format, each vector on one line, elements separated by a space, each lines should have an equal number of elements.
labels.txt - trained vector labels: format, each label on one line in the same order the corresponding vectors appear in vectors.txt


To run our program: 

There are two main programs to be run.

The first is parallelLDA.py. To run the program, you use the straightforward "python parallelLDA.py" command in your terminal. To run this on a particular file, edit parallelLDA.py so that it contains the path to whichever text file you would like to test. This text file (UTF-8) should be free of punctuation and symbols, only containing letters. Ignoring this should not result in an error but rather might return incorrect results, as the word "disorder" is treated as a different word than "disorder," (comma following word). 

The second is wordvis.py. Similarly, it can be run using "python wordvis.py" from the terminal. It visualizes the trained vectors based on vectors.txt and labels.txt. To use a different data set, simply change the file path to what you want to be visualized in lines 9 and 10. 
The file word2vec.py actually trains the vectors, and it works, sometimes. It seems to randomly run into issues with unicode. As in I can save the text file then run word2vec.py successfully, then immediately run it again with it breaking in error that it doesn't understand some unicode that appeared. This has yet to be resolved so there are no guarantees that it will work upon experimentation. The vectors and labels that we used, however, were trained with our own word2vec.py in one of the instances that it worked.