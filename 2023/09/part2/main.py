import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import pprint

pp = pprint.PrettyPrinter(width=200).pprint

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            m = re.findall(r"-?\d+", line)
            ret.append([int(d) for d in m])
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

diffs = []
s = 0

for history in data:
    allzero = False
    diffs.append(history)

    while not allzero:
        allzero = True
        diff = []

        for i in range(1, len(diffs[-1]), 1):
            val = diffs[-1][i] - diffs[-1][i-1]
            diff.append(val)

            if val != 0:
                allzero = False

        diffs.append(diff)

    diffs.reverse()
    goal = 0
    for diff in diffs:
        x = diff[0] - goal
        diff.insert(0, x)
        goal = x

    s += goal

    pp(diffs)
    diffs = []

print(s)
