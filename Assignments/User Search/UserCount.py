'''
Author : Tejas Shinde
MSc CA
SICSR
'''
def userCount(filePath):
    try:
        for line in open(filePath,'r').readlines():
            print("".join(line).split(':')[0])
    except FileNotFoundError:
        print("File not present on the disk")
try:
    filePath = input("Please enter file name/path : ")
    userCount(filePath)
except ValueError:
    print("Please enter a valid string path.")
