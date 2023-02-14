#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    finalNumber = number % -10
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,finalNumber))
else:
    finalNumber = number % 10
if finalNumber > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, finalNumber))
elif finalNumber == 0:
    print("Last digit of {} is {} and is 0".format(number, finalNumber))
