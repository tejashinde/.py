'''
Author : Tejas Shinde
MSc CA
SICSR
PRN 37
'''
from string import ascii_letters,digits
from random import sample,randint

try:
    passwords = int(input("Please enter the number of passwords to be generated : " ))

    for iterator in range(1,passwords+1):
        print("Password " + str(iterator) + " : " + ''.join(sample(ascii_letters,randint(10,18))) + ''.join(sample(digits,randint(1,3))) + ''.join(sample('!@#$%^&*()[]{}"_-=.',randint(1,3))))

except ValueError:
    print("Please enter a valid integer value.")
