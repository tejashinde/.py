 # setA = set([])
 # setB = set([])
 # for line in open("f1.txt","r").readlines():
 #     setA.add(line.strip())
 # for line in open("f2.txt","r").readlines():
 #     setB.add(line.strip())
 # print(setA.intersection(setB))
'''
Author : Tejas Shinde
18030142037
SICSR MSc CA

Will find all the common elements from 2 files f1 and f2
'''
print("".join(set(open("f1.txt","r").readlines())&(set(open("f2.txt","r").readlines()))))
