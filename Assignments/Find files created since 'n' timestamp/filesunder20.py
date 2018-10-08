'''
Author : Tejas Shinde
MSc CA
SICSR
PRN 37
'''
# Will print all the files created under 20 minutes
# st_ctime gives us the creation time as per the operating system time
# 1200 is 20 minutes (20 x 60)
from datetime import datetime
from os import walk,stat
try:
    path = input("Please enter the directory name/path : ")
    for file in list(walk(path))[-1][-1]:
        if((datetime.now().timestamp() - stat(path + "/" + file).st_ctime) < (20 * 60)):
            print(file)
except IndexError:
    print("Incorrect directory name/path.")
