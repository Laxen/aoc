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

pic = [2 for _ in range(width*height)]
print(pic)

for layer in range(img.shape[0]):
    print("dealing with", img[layer])
    f = img[layer].flatten()
    for i, x in enumerate(f):
        if x != 2 and pic[i] == 2:
            pic[i] = x
            print(i, "is", x)

pic = np.array(pic)
pic = pic.reshape(height, width)
pic = np.where(pic == 1, "o", " ")

np.set_printoptions(linewidth=np.inf)
print(pic)
