import sys
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import re
import itertools, time

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    result = {}
    with open(input_file, "r") as f:
        for line in f:
            line = line.strip()
            node, left, right = re.findall(r"(.*) = \((.*), (.*)\)", line)[0]
            result[node] = (left, right)
    return result

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

# data = {"AAA": ("BBB", "CCC"),
#         "BBB": ("DDD", "EEE"),
#         "CCC": ("ZZZ", "GGG"),
#         "DDD": ("DDD", "DDD"),
#         "EEE": ("EEE", "EEE"),
#         "GGG": ("GGG", "GGG"),
#         "ZZZ": ("ZZZ", "ZZZ")}

# data = {"AAA": ("BBB", "BBB"),
#         "BBB": ("AAA", "ZZZ"),
#         "ZZZ": ("ZZZ", "ZZZ")}
#
# instruction = "LLR"

instruction = "LRRRLRRLRRLRRLLLRRRLRRLLRRRLRLLLRRLRLRLRLRLRLRLRRRLLLRRLRRRLRLLRRRLRRRLRRRLLRRRLRLRRRLRRLRRRLLRLLRLLRRRLRRRLRRLRLRLLRLRRLRRRLRRRLRLRLRLRRLRLRLLLRRRLRLRLRRRLRRRLRRRLRLLLRRLRLRLRLRLLLRRRLRRLRRLRLRLRRRLRLRRRLRRRLRRRLRLRRRLLLRRLRRRLRRLLRLRRLRRLRRRLLLRRLRRLRRLRLRRRLLLRLRRRR"

node = "AAA"
steps = 0
for i in itertools.cycle(instruction):
    if i == "R":
        node = data[node][1]
    elif i == "L":
        node = data[node][0]
    else:
        raise ValueError(f"Unknown instruction: {i}")
    steps += 1

    print(node)
    if node == "ZZZ":
        break

    #time.sleep(1)

print(steps)
