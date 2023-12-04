import sys
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import re

np.set_printoptions(linewidth=np.inf)

class Card:
    def __init__(self, id, winning, mine):
        self.id = id
        self.winning = winning
        self.mine = mine

    def __repr__(self):
        return f"Card({self.id}, {self.winning}, {self.mine})"

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for l in f:
            m = re.match(r"Card\s+(\d+): (.*) \| (.*)", l)
            id = int(m.group(1))
            winning = m.group(2).strip().split()
            mine = m.group(3).strip().split()
            ret.append(Card(id, winning, mine))
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

s = 0
for c in data:
    winning = 0
    for m in c.mine:
        if m in c.winning:
            if winning == 0:
                winning = 1
            else:
                winning *= 2
    s += winning
print(s)
