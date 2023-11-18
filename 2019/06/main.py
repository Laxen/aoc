import sys
from pyhelpers import Parser


def make_data(input_file):
    with open(input_file, "r") as f:
        data = f.read().splitlines()
    return data

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

class Body:
    def __init__(self):
        self.orbits = []

    def add_orbit(self, body):
        self.orbits.append(body)

    def n_orbits(self):
        orbits = len(self.orbits)
        for body in self.orbits:
            orbits += body.n_orbits()
        return orbits

bodies = {}

for line in data:
    body1, body2 = line.split(")")

    if body1 not in bodies:
        bodies[body1] = Body()
    if body2 not in bodies:
        bodies[body2] = Body()

    bodies[body2].add_orbit(bodies[body1])

sum_orbits = 0
for name, body in bodies.items():
    sum_orbits += body.n_orbits()
print(sum_orbits)
