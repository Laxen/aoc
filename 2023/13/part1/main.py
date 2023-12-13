import sys, re, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
from pprint import pprint

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    ret.append([])
    with open(input_file, "r") as f:
        for line in f:
            if line.strip() == "":
                ret.append([])
            else:
                element = line.strip()
                ret[-1].append(list(element))
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

def fold(pattern):
    for i in range(1, len(pattern)):
        top = pattern[:i]
        bottom = pattern[i:]
        bottom.reverse()

        # print(i, "top")
        # pprint(top)
        # print(i, "bottom")
        # pprint(bottom)
        # print(i, "bottom[:i]")
        # pprint(bottom[:i])
        # print()

        if len(top) > len(bottom):
            if top[len(top) - len(bottom):] == bottom:
                return i
        else:
            if top == bottom[len(bottom) - len(top):]:
                return i


        # if top == bottom:
        #     return i
        # if top[1:] == bottom:
        #     return i
        # if top == bottom[1:]:
        #     return i
    return None

def foldold(pattern):
    for i in [len(pattern) // 2, len(pattern) // 2 + 1]:
        top = pattern[:i]
        bottom = pattern[i:]
        # pprint(top)
        bottom.reverse()
        # pprint(bottom)
        # print()

        if top == bottom:
            return i
        if top[1:] == bottom:
            return i
        if top == bottom[1:]:
            return i
    return None

s = 0

# print(fold(data[2]))

print("Horizontal")
for pattern in data:
    row = fold(pattern)
    s += 100 * row if row else 0

print("Vertical")
for pattern in data:
    pattern = list(map(list, zip(*pattern)))
    col = fold(pattern)
    s += col if col else 0

print(s)

# for pattern in data:
#     matches = 0
#     splitter = None
#     for i in range(len(pattern)):
#         for n in range(i, len(pattern)):
#             if i == n:
#                 continue
#
#             if pattern[i] == pattern[n]:
#                 matches += 1
#                 if abs(i - n) == 1:
#                     splitter = i + 1
#
#     if matches >= len(pattern) // 2:
#         print("HORIZONTAL", splitter)
#
# for pattern in data:
#     matches = 0
#     splitter = None
#     pattern = list(map(list, zip(*pattern)))
#     for i in range(len(pattern)):
#         for n in range(i, len(pattern)):
#             if i == n:
#                 continue
#
#             if pattern[i] == pattern[n]:
#                 matches += 1
#                 if abs(i - n) == 1:
#                     splitter = i + 1
#
#     print(matches, len(pattern) // 2)
#     if matches >= len(pattern) // 2:
#         print("Vertical", splitter)
