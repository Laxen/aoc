import sys
import numpy as np
from collections import defaultdict
from pyhelpers import Parser
import re

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    with open(input_file) as file:
        for line in file:
            ret.append(re.findall(r"\d", line))
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

s = sum([int(row[0] + row[-1]) for row in data])
print(s)
