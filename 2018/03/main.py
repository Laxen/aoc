import sys
import numpy as np
from pyhelpers import Parser

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    return Parser.ints_to_list(input_file)

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

class Claim:
    def __init__(self, id, left, top, width, height):
        self.id = id
        self.left = left
        self.top = top
        self.width = width
        self.height = height

        self.map = dict()
        for x in range(self.left, self.left + self.width):
            for y in range(self.top, self.top + self.height):
                self.map[(y, x)] = 1

    def merge_map(self, map):
        for c, _ in self.map.items():
            if c in map:
                map[c] += 1
            else:
                map[c] = 1

    def check_map(self, map):
        for c, _ in self.map.items():
            if map[c] > 1:
                return False
        return True

    def __repr__(self):
        return f"{self.id}"

claims = []
for i in range(0, len(data), 5):
    claims.append(Claim(*data[i:i+5]))

map = dict()
for claim in claims:
    claim.merge_map(map)

for claim in claims:
    check = claim.check_map(map)
    if check:
        print(claim.id)
