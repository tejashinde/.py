'''
Author : Tejas Shinde
MSc CA
SICSR
PRN 37
'''
try:
    filePath = input("Please enter file path : ")
    for word in open(filePath,"r").read().split():
        if(word.istitle()):
            print('Z' + word[1::] + word[0])
        elif(not word.istitle()):
            print('z' + word[1::] + word[0])
except FileNotFoundError:
    print("No file found.")
