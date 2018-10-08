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
import os
try:
    a = 0
    directoryList = ['a','b','c']
    os.mkdir('a')
    print('a')
    print("+------",end = "")
    os.chdir('a')
    for i in directoryList:
        os.mkdir(i)
        if (i != 'a'):
            print("+------",end = "")
        print(i)
        print("|      +------",end = "")
        os.chdir(i)
        for j in directoryList:
            os.mkdir(j)
            if(j != 'a'):
                print("|      +------",end = "")
            print(j)
        os.chdir("..")

except FileExistsError:
    print("File Already Exists")
