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
# instruction = "LR"

instruction = "LRRRLRRLRRLRRLLLRRRLRRLLRRRLRLLLRRLRLRLRLRLRLRLRRRLLLRRLRRRLRLLRRRLRRRLRRRLLRRRLRLRRRLRRLRRRLLRLLRLLRRRLRRRLRRLRLRLLRLRRLRRRLRRRLRLRLRLRRLRLRLLLRRRLRLRLRRRLRRRLRRRLRLLLRRLRLRLRLRLLLRRRLRRLRRLRLRLRRRLRLRRRLRRRLRRRLRLRRRLLLRRLRRRLRRLLRLRRLRRLRRRLLLRRLRRLRRLRLRRRLLLRLRRRR"

start_nodes = []
for node in data:
    if node[-1] == "A":
        start_nodes.append(node)

steppers = {0: [0], 1: [0], 2: [0], 3: [0], 4: [0], 5: [0]}

steps = 0
nodes = start_nodes
for i in itertools.cycle(instruction):
    new_nodes = []
    for node in nodes:
        if i == "R":
            new_nodes.append(data[node][1])
        elif i == "L":
            new_nodes.append(data[node][0])
        else:
            raise ValueError(f"Unknown instruction: {i}")
    steps += 1

    # print(new_nodes)

    breaker = True
    for ni, n in enumerate(new_nodes):
        steppers[ni][-1] += 1
        if n[-1] == "Z":
            steppers[ni].append(0)
        if len(steppers[ni]) < 3:
            breaker = False

        nodes = new_nodes

    if breaker:
        break

steps = 1
for _, stepp in steppers.items():
    if stepp[0] == 0:
        continue

    steps *= stepp[0] // np.gcd(steps, stepp[0])
print(steps)
