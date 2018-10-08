# Number to be added should be consecutive in nature


from re import finditer;
fileName = input("\nEnter a file name from pwd or the path to the same : ")
fileOpened = open(fileName,"r")
consList = []
sum = 0
for word in fileOpened.read().split():
    # print(word)
    for iterables in finditer(r'((\d)\2)+',word):
        consList.append(int(word))
# print(consList)
# print("\n")
print("The sum of following consecutive numbers from the file ",end = ": ")
for number in consList:
    sum += number;
    print(number,end=" ")
    # if (number == consList[::-1]):
        # print(number,end = " ")
print ("is " + str(sum))
