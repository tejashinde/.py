#Tejas Shinde
#Symbiosis Institute of Computer Studies and Research
#28th Aug 2018
# a
# +-------a
# |       +-------a
# |       +-------b
# |       +-------c
# +-------b
# |       +-------a
# |       +-------b
# |       +-------c
# +-------c
# |       +-------a
# |       +-------b
# |       +-------c
from os import mkdir,chdir;
try:
    a = 0
    path = input("Please enter a path : ")
    chdir(path)
    # numInput = input("Please enter number of sub-directories in the above path : ")
    directoryList = ['a','b','c']
    mkdir('a')
    print('a')
    print("+------",end = "")
    chdir('a')
    for i in directoryList:
        mkdir(i)
        if (i != 'a'):
            print("+------",end = "")
        print(i)
        print("|      +------",end = "")
        chdir(i)
        for j in directoryList:
            mkdir(j)
            if(j != 'a'):
                print("|      +------",end = "")
            print(j)
        chdir("..")
except FileExistsError:
    print("File Already Exists")
