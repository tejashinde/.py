
dict = {}
try:
    for n in range (100,1000):
        for d in range(100,1000):

            nstr = str(n)
            dstr = str(d)

            if(int(dstr[-1]) == 0):
                continue
            if(int(nstr[0])/int(dstr[-1]) == n/d):
                print("%s / %s = %f" % (nstr,dstr,(n/d)) + " and " + "%d / %d = %f" % (n,d,(n/d)))
            else:
                pass
    print(dict)
except ValueError:
    print("Please enter a valid number")
