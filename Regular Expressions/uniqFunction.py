# uniqset = set([])
# for line in open("test.txt","r").readlines():
#     uniqset.add(line.strip())
# for i in sorted(uniqset):
#     print(i)
    # dict[line.strip()] = 0
# for i in (sorted(dict.keys())):
    # print(i)
dict2 = {}
dict = {}
for line in open("test.txt",'r'):
    dict[line.strip()] = line.strip()
    # print(dict.keys())
    list.append(dict[line.strip()])
    if(line.strip() in dict.keys()):
        dict2[line.strip()] = 0
        list.append(dict2[line.strip()])
print(list)
        # print(line)
# for i in dict.keys():
#     print(i)
# for j in dict2.keys():
#     print(j)
