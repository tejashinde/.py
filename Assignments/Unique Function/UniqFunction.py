'''
Author : Tejas Shinde
18030142037
SICSR MSc CA

Will act as the uniq command in linux (cat test | uniq)
'''
def uniq(filePath):
    try:
        list = []
        for lines in open(filePath,"r").readlines():
            list.append(lines.strip())
        for index in range(0,len(list)):
            if (index == len(list)-1):
                print(list[index])
                break
            if(list[index] != list[index+1]):
                print(list[index])
    except FileNotFoundError:
        print("File not present on the disk")

filePath = input("Please enter file name/path : ")
uniq(filePath)
