# Will take multiple list values
# def avg(*largs):
#     print(type(largs),largs)
#     return sum(largs)/len(largs)
#
# # Will set a,b,c to default and if b is defined in params it will take the new value
# def sum (a = 1, b = 2, c = 3):
#     print (a + b + c)
#
# # If you want to pass a dictionary in the parameters
# def arguements (*largs,**kargs):
#     print('kargs',kargs)
#     print('largs',largs)
#     print(kargs['q'])
#     print(largs[0])

def maximum(*largs):
    maxnum = 0
    for number in largs:
        if (number > maxnum):
            number = maxnum
    print(maxnum)

maximum(1,2,3,4,5,6,7)
# arguements(1,2,q=10)

# Python will convert params in *largs and **kargs
