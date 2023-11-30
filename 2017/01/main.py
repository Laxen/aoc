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

sum = 0
i = 0
while True:
    if i == len(data)-1:
        if data[i] == data[0]:
            sum += int(data[i])
        break

    if data[i] == data[i+1]:
        sum += int(data[i])

    i += 1

print("Part 1:", sum)
