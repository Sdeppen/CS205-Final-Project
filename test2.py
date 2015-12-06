import findspark
findspark.init()
from pyspark import SparkContext
from pyspark.mllib.feature import Word2Vec

sc = SparkContext(appName='Word2Vec')
inp = sc.textFile("dsm-iv-2-8.txt").map(lambda row: row.split(" "))
print inp.take(1) 

word2vec = Word2Vec()
model = word2vec.fit(inp)

synonyms = model.findSynonyms('motor', 10)

for word, cosine_distance in synonyms:
    print("{}: {}".format(word, cosine_distance))
