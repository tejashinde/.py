list = [50,2,1,9]
l2 = []
for iterable in list:
    for char in str(iterable)[0]:
        for index in range(0,len(list)):
            if(index == len(list)):
                continue
            if(int(char) > int(str(iterable)[index])):
                l2.append(char)

            # if(int(str))
print(l2)
