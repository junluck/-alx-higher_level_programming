#!/usr/bin/python3
import random
number = random.randint(-10,10)
if number > 0 :
    num = number
    print ("{} is positive".format(num))
elif number < 0:
    num = number
    print ("{} is negative".format(num))
else:
    num = number 
    print ("{} is zero".format(num))
