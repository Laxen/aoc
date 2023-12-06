import sys
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import re

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    l = Parser.ints_to_list(input_file)
    return l[len(l)//2:], l[:len(l)//2]

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

dist = data[0]
time = data[1]

n_record_beat = []
for i, time in enumerate(time):
    n_record_beat.append(0)
    for t in range(0, time):
        d = t * (time - t)
        if d > dist[i]:
            n_record_beat[i] += 1

sum = 1
for i in n_record_beat:
    sum *= i
print(sum)
