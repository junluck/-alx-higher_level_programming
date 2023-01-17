#!/usr/bin/python3
import random
number = random.randint(-10,10)
if number > 0 :
    num = number
    print ("%s is positive" % num)
elif number == 0:
    num = number
    print ("%s is zero" % num)
elif number < 0:
    num = number 
    print ("%s is negative" % num)
