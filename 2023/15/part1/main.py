import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
from pprint import pprint

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        return f.read().strip().split(",")

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def hash(msg):
    current_value = 0

    for c in msg:
        current_value += ord(c)
        current_value *= 17
        current_value %= 256

    return current_value

boxes = defaultdict(list)

for step in data:
    if "=" in step:
        label, focal = step.split("=")
        n = hash(label)
        for i, lens in enumerate(boxes[n]):
            if lens[0] == label:
                boxes[n][i] = (label, int(focal))
                break
        else:
            boxes[n].append((label, int(focal)))
    elif "-" in step:
        label = step[:-1]
        n = hash(label)
        for lens in boxes[n]:
            if lens[0] == label:
                boxes[n].remove(lens)
                break

s = 0
for box_index, box in boxes.items():
    for lens_index, lens in enumerate(box):
        s += (1 + box_index) * (lens_index + 1) * lens[1]

print(s)
