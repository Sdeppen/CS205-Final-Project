import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec

sc = SparkContext(appName='Word2Vec')
inp = sc.textFile("dsm-iv-lc-nosym.txt").map(lambda row: row.split(" "))
print inp.take(1) 

word2vec = Word2Vec()
model = word2vec.fit(inp)

word_min_freq = 500
synonyms_per_word = 50

word_list = []
num_list = []
wordcnt = []
counter = 1
file = open("dsmnum.txt","w") #file to write file in word id numbers 
with open('DSM.txt','r') as f:
    for line in f:
        for word in line.split(): #if already read at least once
            if word in word_list:
                index = word_list.index(word)
                file.write("%s " %(num_list[index]))
                wordcnt[index] += 1
            else: #if new word
            	if len(word) > 4:
	                word_list.append(word)
	                num_list.append(counter)
	                wordcnt.append(1)
	                counter += 1
	                file.write("%s " %(counter))
file.close()
words_greater_100 = []
for i in range(len(wordcnt)):
    if (wordcnt[i] > word_min_freq):
        words_greater_100.append(word_list[i])

for idx in range(len(words_greater_100)):
	synonyms = model.findSynonyms(words_greater_100[idx], synonyms_per_word)
	print str(idx) + " : " + words_greater_100[idx]
	for word, cosine_distance in synonyms:
		if ord(word[0]) < 128:
			print("{}: {}".format(word, cosine_distance))

sc.stop()

