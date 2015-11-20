import findspark
findspark.init()
from pyspark import SparkContext
sc = SparkContext()
import random

def sample(p): 
    x, y = random.random(), random.random()
    return 1 if x*x + y*y < 1 else 0
NUM_SAMPLES = 10000
count = sc.parallelize(xrange(0, NUM_SAMPLES)).map(sample).reduce(lambda a, b: a + b)
print "Pi is roughly %f" % (4.0 * count / NUM_SAMPLES)
