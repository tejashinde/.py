#Tejas Ashok Shinde 37
def calculatePi(n):
    p=0.0
    numerator = 4.0
    try:
        if (int(n)<=0):
            print("Please enter a positive integer and not zero")
            return
    except ValueError:
        print("Please enter a positive integer only")
        return
    for i in range(1,int(n)+1):
        if (i % 2 == 0):
            p -= (numerator / (2 * i - 1))
        else:
            p += (numerator / (2 * i - 1))
    print(p)
n = input("Please enter a positive integer range to calculate pi as follows if 3 is entered (4/1) - (4/3) + (4/5) : ")
calculatePi(n)
