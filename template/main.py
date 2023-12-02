import sys
import numpy as np
from collections import defaultdict
from pyhelpers import Parser
import re

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
