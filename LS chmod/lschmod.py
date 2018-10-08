dict = {'r' : 0 , 'w' : 0 , 'x' : 0}
for line in open("ls.txt","r").readlines():
    for char in line.split()[0]:
        while(True):
            if char in dict:
                dict[char] += 1
                break
            else:
                # continue
                break
    if(char == 'r'):
        chmod = (dict[char]) * 4
    elif(char == 'w'):
        chmod = (dict[char]) * 2
    elif(char == 'x'):
        chmod = (dict[char])
    else:
        continue
print(chmod)
print(dict)
