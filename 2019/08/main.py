import sys
from pyhelpers import Parser
import numpy as np

def make_data(input_file):
    with open(input_file, "r") as f:
        return f.readline().rstrip()

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

width = 25
height = 6

img = np.array([int(x) for x in data])
img = img.reshape((int(len(data)/(width*height)), width, height))
print(img)
zero_cnt = np.sum(img == 0, axis=(1, 2))
zero_i = np.argmin(zero_cnt)

n_ones = np.sum(img[zero_i] == 1)
n_twos = np.sum(img[zero_i] == 2)
print(n_ones * n_twos)
