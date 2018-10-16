#ODD (minus cube root)
#EVEN (plus square)

def calculateVal(name):
    sum = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    print(name)
    name = name.lower()

    for n in name:
        t = letters.find(n)
        if t==0:
            sum -= -1
            round(sum,4)
        elif t > -1 and (t+1)%2 == 0:
            sum += (t + 1) ** 2
            round(sum,4)
        elif t>-1 and (t+1)%2 != 0:
            sum -= (t + 1) ** round(1/3,2)
            round(sum,2)
    print(round(sum,2))

try:
    name = "Tejas"
    calculateVal(name)
except AttributeError:
        print("Please initiate name to String datatype only")
