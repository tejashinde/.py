
filename = "test.txt"
file = open(filename, 'r')
lines = file.readlines()
wordcount = 0
for line in lines:
    for word in lines.split:
        wordcount += 1
print(wordcount)
