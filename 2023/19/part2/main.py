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

def work(workflow, mms):
    if workflow == "A":
        return [mms]
    if workflow == "R":
        return []

    mms_list = []

    neg_mms = mms.copy()
    for condition in data[workflow]:
        sp = condition.split(":")
        new_mms = neg_mms.copy()

        if len(sp) == 2:
            attr = sp[0][0]
            if sp[0][1] == "<":
                new_mms[attr] = (new_mms[attr][0], min(new_mms[attr][1], int(sp[0][2:])))
                neg_mms[attr] = (max(neg_mms[attr][0], int(sp[0][2:]) - 1), neg_mms[attr][1])
            else:
                new_mms[attr] = (max(new_mms[attr][0], int(sp[0][2:])), new_mms[attr][1])
                neg_mms[attr] = (neg_mms[attr][0], min(neg_mms[attr][1], int(sp[0][2:]) + 1))

            mms_list.extend(work(sp[1], new_mms))
        else:
            mms_list.extend(work(sp[0], new_mms))

    return mms_list

mms = defaultdict(lambda: (0, 4001))
mms_list = work("in", mms)

# pprint(mms_list)

s = 0
for d in mms_list:
    combos = 1

    for attr in ["x", "m", "a", "s"]:
        diff = d[attr][1] - d[attr][0] - 1
        combos *= diff

    pprint(d)
    print(combos)
    s += combos
print(s)
