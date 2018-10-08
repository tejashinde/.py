# Author : Tejas Ashok Shinde
# Symbiosis Institute of Computer Studies and Research
# 2nd Sept 2018
from collections import Counter;
data = []
for line in open('test.txt','r'):
    data.extend(line.split())


print(data)
count = Counter(data)
print(count)
