'''
Author : Tejas Shinde
MSc CA
SICSR
PRN 37
'''
from os import listdir,rename
dirPath = input("Please enter directory path/directory name : ")

try:
    for filenames in listdir(dirPath):
        rename(dirPath + "/" + filenames,dirPath + "/" + filenames.replace(" ","_"))
    print("Success")

except FileNotFoundError:
    print("No such path/directory name found.")
