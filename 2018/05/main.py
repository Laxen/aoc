import sys
import numpy as np
from collections import defaultdict
from pyhelpers import Parser
from string import ascii_uppercase

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
        c1 = data[i]
        c2 = data[i-1]

        if c1 != c2 and (c1.lower() == c2 or c1 == c2.lower()):
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

origdata = data
lengths = []

for c in ascii_uppercase:
    print(c)
    data = origdata
    data = data.replace(c, "")
    data = data.replace(c.lower(), "")

    prevdata = reduce(data)
    while prevdata != data:
        data = prevdata
        prevdata = reduce(data)

    lengths.append(len(data))

print(min(lengths))
