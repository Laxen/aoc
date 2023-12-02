import sys
import numpy as np
from collections import defaultdict
from pyhelpers import Parser
import re

np.set_printoptions(linewidth=np.inf)

class Game:
    def __init__(self, id):
        self.id = id
        self.rounds = []

def make_data(input_file):
    games = []
    with open(input_file, "r") as f:
        for l in f:
            m = re.search(r"Game (\d+)", l)
            id = int(m.group(1))
            g = Game(id)

            rounds = l.split(";")
            for round in rounds:
                m = re.search(r"(\d+)\sred", round)
                reds = int(m.group(1)) if m else 0

                m = re.search(r"(\d+)\sgreen", round)
                greens = int(m.group(1)) if m else 0

                m = re.search(r"(\d+)\sblue", round)
                blues = int(m.group(1)) if m else 0

                g.rounds.append((reds, greens, blues))

            games.append(g)

    return games

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

s = 0
for g in data:
    reds = 0
    greens = 0
    blues = 0
    for colors in g.rounds:
        reds = max(reds, colors[0])
        greens = max(greens, colors[1])
        blues = max(blues, colors[2])

    if reds <= 12 and greens <= 13 and blues <= 14:
        s += g.id

print(s)
