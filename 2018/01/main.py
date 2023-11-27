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

print(data)

res = 0
res_list = []
res_i = 0
while True:
    d = data[res_i % len(data)]
    res += d
    if res in res_list:
        break
    res_list.append(res)
    res_i+=1

print(res)
