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
            line = line.replace("one", "o1e")
            line = line.replace("two", "t2o")
            line = line.replace("three", "t3e")
            line = line.replace("four", "f4r")
            line = line.replace("five", "f5e")
            line = line.replace("six", "s6x")
            line = line.replace("seven", "s7n")
            line = line.replace("eight", "e8t")
            line = line.replace("nine", "n9e")
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
