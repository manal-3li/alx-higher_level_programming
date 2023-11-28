#!/usr/bin/python3

def hex_convert(num):
    result = hex(num)
    print("[{:<3}] = {}".format(num, result))

for num in range(0, 99):
    hex_convert(num)
