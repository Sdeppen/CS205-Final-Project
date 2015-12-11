import numpy as Math
import pylab as Plot
import tsne as visualize
from PIL import Image

# Functions in tsne taken from http://lvdmaaten.github.io/tsne/

# Load in labels and vectors for corresponding labels
vector_matrix = Math.loadtxt("vectors.txt")
labels = [line.strip() for line in open("labels.txt")]

rows = [labels.index(word) for word in labels]
target_matrix = vector_matrix[rows,:]

# Run the t-SNE reducing to 2 dimensions
reduced_matrix = visualize.tsne(vector_matrix,2)

# Plot the figure
Plot.figure(figsize=(20, 20), dpi=10)
max_x = Math.amax(reduced_matrix, axis=0)[0]
max_y = Math.amax(reduced_matrix, axis=0)[1]
Plot.xlim((-max_x,max_x))
Plot.ylim((-max_y,max_y))

Plot.scatter(reduced_matrix[:, 0], reduced_matrix[:, 1], 20);

# Add labels
for row_id in range(0, len(rows)):
    target_word = labels[rows[row_id]]
    x = reduced_matrix[row_id, 0]
    y = reduced_matrix[row_id, 1]
    Plot.annotate(target_word, (x,y))

# Save and open the figure
Plot.savefig("word2vec_vis.png")
f = Image.open("word2vec_vis.png").show()