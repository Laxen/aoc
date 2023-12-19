import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
from pprint import pprint

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = {}
    parts = []
    with open(input_file, "r") as f:
        for line in f:
            if line == "\n":
                break

            name, rest = line.split("{")
            conditions = rest.split(",")
            conditions = [c.strip() for c in conditions]
            conditions[-1] = conditions[-1][:-1]

            ret[name.strip()] = conditions

        for line in f:
            attributes = line.split(",")
            attributes = [a.strip() for a in attributes]
            attributes[-1] = attributes[-1][:-1]
            attributes[0] = attributes[0][1:]

            di = {}
            for attr in attributes:
                di[attr.split("=")[0]] = int(attr.split("=")[1])
            parts.append(di)

    return ret, parts

if len(sys.argv) > 1:
    print("INPUT\n")
    data, parts = make_data("input")
else:
    print("EXAMPLE\n")
    data, parts = make_data("example")

# -----------------

def process(workflow, part):
    if workflow == "A" or workflow == "R":
        return workflow

    workflow = data[workflow]

    x = part["x"]
    m = part["m"]
    a = part["a"]
    s = part["s"]

    for condition in workflow:
        cond_split = condition.split(":")

        if len(cond_split) == 2:
            c1 = cond_split[0]
            b = eval(c1)
            if b:
                return process(cond_split[1], part)
        else:
            return process(cond_split[0], part)

s = 0
for part in parts:
    if process("in", part) == "A":
        s += part["x"] + part["m"] + part["a"] + part["s"]

print(s)
