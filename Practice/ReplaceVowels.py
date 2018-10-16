file = open("test.txt",'r')
file2 = open("test.txt")
vowels = ['a','e','i','o','u','','','']
data = []
for i in file:
    for word in i.split():
        for char in word:
            # print(char)
            for k in range(0,6):
                if(char == vowels[k]):
                    data.append(char.replace(vowels[k],vowels[k+1]))
                else:
                    data.append(char)
print(data)
                # elif(char == 'u'):
                    # print(char.replace('u','a'))

                # if(char == v):
                    # char.replace(v,v+1)
                #     print(char)
                    # file.write(chr(v+1))
                    # print(chr(v+1))
