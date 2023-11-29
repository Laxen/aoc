import sys
import numpy as np
from collections import defaultdict
from pyhelpers import Parser

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        return f.readline().strip()

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def reduce(data):
    i = 1
    newdata = ""
    while True:
        print(i, len(data))
        c1 = data[i]
        c2 = data[i-1]

        if c1 != c2 and (c1.lower() == c2 or c1 == c2.lower()):
            print("React", c1, c2)
            i += 1
        else:
            newdata += data[i-1]

        if i < len(data) - 1:
            i += 1
        else:
            if i < len(data):
                newdata += data[i]
            break

    return newdata


prevdata = reduce(data)
while prevdata != data:
    data = prevdata
    prevdata = reduce(data)
print(len(data))
