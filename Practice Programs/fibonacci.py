def isFibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return isFibonacci(n-1) + isFibonacci(n-2)
try:
    number = int(input("Enter number of elements from fibonacci series to be printed from 0,1,1,3...... : "))
    l = []
    for i in range(number):
        l.append(isFibonacci(i))
    print (l)
except ValueError:
    print("Please strictly enter an integer value only")
