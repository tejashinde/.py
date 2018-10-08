inputString = input("Please enter a string : ")
wordList = inputString.lower().split(" ");

wordCount = {}
for i in wordList:
        wordCount[i] = 0

for i in wordList:
        wordCount[i] += 1

print (wordCount)
