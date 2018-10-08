import re;
f = open("test.txt","r")
data = f.readlines()
# print(f.readlines())
list = []
dict = {}
for line in data:
    dict[re.findall('\w+',line)[0]] = 0
    dict[line[0]]
    # print(int(re.findall('\w+',line)[2]))
    # for word in line.split(','):
        # list.append(word)
        # for i in list:
        #     for val in range(0,100):
        #     # print(i)
        #         dict[i] = val
        #         val -= 1
print(dict)
