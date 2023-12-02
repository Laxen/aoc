import sys
import numpy as np
from collections import defaultdict
from pyhelpers import Parser
import re
import time

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file) as file:
        return file.read().splitlines()

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------


sum = 0
for l in data:
    first = -1
    last = -1
    newl = l
    alpha = ""
    print(l)
    for n in newl:
        if n.isnumeric() == False:
            alpha += n
            if "one" in alpha:
                alpha = n
                n = 1
            elif "two" in alpha:
                alpha = n
                n = 2
            elif "three" in alpha:
                alpha = n
                n = 3
            elif "four" in alpha:
                alpha = n
                n = 4
            elif "five" in alpha:
                alpha = n
                n = 5
            elif "six" in alpha:
                alpha = n
                n = 6
            elif "seven" in alpha:
                alpha = n
                n = 7
            elif "eight" in alpha:
                alpha = n
                n = 8
            elif "nine" in alpha:
                alpha = n
                n = 9
            else:
                continue

        if first == -1:
            first = int(n)
            last = int(n)
        else:
            last = int(n)
    print(first, last)
    sum += int(str(first) + str(last))

print(sum)
