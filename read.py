word_list = []
num_list = []
wordcnt = []
counter = 1
file = open("dsmnum.txt","w") #file to write file in word id numbers 
with open('dsm-iv-lc-nosym.txt','r') as f:
    for line in f:
        for word in line.split(): #if already read at least once
            if word in word_list:
                index = word_list.index(word)
                file.write("%s " %(num_list[index]))
                wordcnt[index] += 1
            else: #if new word
                word_list.append(word)
                num_list.append(counter)
                wordcnt.append(1)
                counter += 1
                file.write("%s " %(counter))
file.close()

for i in range(len(wordcnt)):
    if (wordcnt[i] > 100):
        print wordcnt[i], word_list[i]
        
#write wordcounts to new file
#filewc = open("wordcount.txt", "w")
#idx = 0
#for num in wordcnt:
#    filewc.write("%s " %(num))
#    idx += 1
#filewc.close()
