
import math
import os
import random
import re
import sys


def drop(el, val, z):
    x = (el-val) // z
    return x, el - x * z

def set_to_val(arr, val):
    steps = 0
    for el in arr:
        s5, el = drop(el, val, 5)
        s2, el = drop(el, val, 2)
        s1, _ = drop(el, val, 1)
        steps += s5 + s2 + s1
    return steps
        

def equal(arr):
    z = min(arr) 
    return min(set_to_val(arr, z-i) for i in range(5))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
