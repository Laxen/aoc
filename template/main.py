import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
from pprint import pprint

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        pass

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

print(data)
