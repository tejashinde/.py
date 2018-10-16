n1 = input("Please enter the a number")

try:
    def CheckIfPrime(number):
        if number > 1:
            for i in range(2,number):
                if(number % i == 0):
                    print(number + "is not a prime number")
                    break
                else:
                    print(number + "is a prime number")
        else:
            print(number + "is a prime number")
except ValueError:
    print("Please enter a valid integer")