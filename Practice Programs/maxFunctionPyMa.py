# Tejas Shinde
# Symbiosis Institute of Computer Studies and Research
# 2nd Sept 2018
def maxnum(*largs):
    try:
        maximum = 0
        for element in largs:
            # STRING
            if(type(element) == str):
                numint = float(element)
                if(numint > maximum):
                    maximum = numint
             # INTEGER
            if(type(element) == int):
                if(element > maximum):
                    maximum = element
            # LIST
            elif(type(element) == list):
                for j in element:
                    if(type(j) == str):
                        numint = float(j)
                        if(numint > maximum):
                            maximum = numint
                    elif(type(j) == int):
                        if(j > maximum):
                            maximum = j
            # TUPLE
            elif (type(element) == tuple):
                for k in element:
                    if(type(k) == str):
                        numint = float(k)
                        if(numint > maximum):
                            maximum = k
                    elif(type(k) == int):
                        if(k > maximum):
                            maximum = k
        print (maximum)
    except ValueError:
        print("Invalid value")

maxnum(1,'8',-1,[1,2,3,10,'100'],(1,1000,'2000'))
