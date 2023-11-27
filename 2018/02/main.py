import sys
import numpy as np
from pyhelpers import Parser

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        return [line.rstrip() for line in f]

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

for a in data:
    for b in data:
        if a == b:
            continue

        count = 0
        res = ""
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
            else:
                res += a[i]

            if count > 1:
                break
        else:
            print(res)
            exit()
