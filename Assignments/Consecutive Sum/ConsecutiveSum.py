'''
Author : Tejas Shinde
18030142037
SICSR MSc CA

Will calculate the sum of numbers which have consecutive nature in the file
'''
from re import finditer;
try:
    def consecutiveSum(filePath):
        consList = []
        sum = 0
        for word in "".join(open(filePath,"r").readlines()).split():
            for iterables in finditer(r'((\d)\2)+',word):
                sum += int(word,10)
                print(word)
        print("Sum : " + str(sum))
except FileNotFoundError:
    print("File not present on the disk")

filePath = input("Please enter file name/path : ")
consecutiveSum(filePath)
