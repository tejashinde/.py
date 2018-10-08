'''
Author : Tejas Shinde
18030142037
SICSR MSc CA

Will act as the uniq + sort command in linux (cat test | sort | uniq)
'''
uniqset = set([])
for line in open("test.txt","r").readlines():
    uniqset.add(line.strip())
for i in sorted(uniqset):
    print(i)
# OR
print("".join(sorted(set(open("test.txt","r").readlines()))))
