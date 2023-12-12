import sys, time
import numpy as np
from collections import defaultdict, deque
from pyhelpers import Parser
import re
from functools import lru_cache
from pprint import pprint

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    ret = []
    with open(input_file, "r") as f:
        for line in f:
            springs, numbers = line.strip().split(" ")
            ret.append((springs, numbers.split(",")))
    return ret

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

@lru_cache(maxsize=None)
def countit(springs, numbers, index, group_length, n_groups):
    if index == len(springs):
        # Last spring is always a . so we don't have to handle it
        return 1 if len(numbers) == n_groups else 0

    if n_groups == len(numbers):
        if springs[index] == "#":
            # We have more groups than allowed, this combo is invalid
            return 0
        # If next spring is ? we have to use . anyway since we can't create more groups
        return countit(springs, numbers, index + 1, 0, n_groups)

    if springs[index] == '#':
        # Continue the group
        return countit(springs, numbers, index + 1, group_length + 1, n_groups)

    if springs[index] == ".":
        if group_length == numbers[n_groups]:
            # Group has ended with correct length
            return countit(springs, numbers, index + 1, 0, n_groups + 1)
        elif group_length == 0:
            # No group, continue
            return countit(springs, numbers, index + 1, 0, n_groups)
        else:
            # Group has ended with incorrect length
            return 0

    # Spring is ?

    if group_length == numbers[n_groups]:
        # Group is full, no choice but to end it
        return countit(springs, numbers, index + 1, 0, n_groups + 1)
    elif group_length == 0:
        # Group is empty, either continue with empty or start a new one
        return countit(springs, numbers, index + 1, 0, n_groups) + \
               countit(springs, numbers, index + 1, 1, n_groups)
    else:
        # Group is in progress, continue it
        return countit(springs, numbers, index + 1, group_length + 1, n_groups)

s = 0
for springs, numbers in data:
    sp = "?".join([springs for _ in range(5)]) + "."
    nu = [int(x) for x in numbers] * 5
    print(sp, nu)
    c = countit(sp, tuple(nu), 0, 0, 0)
    s += c
print(s)
