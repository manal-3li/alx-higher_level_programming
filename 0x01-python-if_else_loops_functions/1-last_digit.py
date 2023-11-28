#!/usr/bin/python3
import random
import math
number = random.randint(-10000, 10000)
def last_digit(number):
    return number % 10 if number > 10 else number % -10
num = last_digit(number)
if num > 5:
    print(f"last digit of {number:d} is {num:d} and is greater than 5")
elif num == 0:
    print(f"last digit of {number:d} is {num:d} and is 0")
else:
    print(f"last digit of {number:d} is {num:d} and is less than 6 and not 0")
