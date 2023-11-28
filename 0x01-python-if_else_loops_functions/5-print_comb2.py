#!/usr/bin/python3


def two_digit(num):
    return str(num).zfill(2)


for num in range(0, 100):
    print("{:s}, ".format(two_digit(num)), end="\n" if i == 99 else ", ")
