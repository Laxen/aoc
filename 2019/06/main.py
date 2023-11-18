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
    def __init__(self, name):
        self.orbits = []
        self.name = name

    def add_orbit(self, body):
        self.orbits.append(body)

    def n_orbits(self):
        orbits = len(self.orbits)
        for body in self.orbits:
            orbits += body.n_orbits()
        return orbits

    def orbit_body(self):
        body = self.orbits[0]
        return body

    def orbit_dict(self):
        ret = dict()
        cnt = 0
        body = self.orbit_body()
        while body.name != "COM":
            ret[cnt] = body
            cnt += 1
            body = body.orbit_body()
        return ret

bodies = {}

for line in data:
    body1, body2 = line.split(")")

    if body1 not in bodies:
        bodies[body1] = Body(body1)
    if body2 not in bodies:
        bodies[body2] = Body(body2)

    bodies[body2].add_orbit(bodies[body1])

you_dict = bodies["YOU"].orbit_dict()
san_dict = bodies["SAN"].orbit_dict()

tot_dist = 0
for you_dist, you_body in you_dict.items():
    for san_dist, san_body in san_dict.items():
        if you_body == san_body:
            print(you_body.name)
            print("you dist:", you_dist)
            print("san dist:", san_dist)
            tot_dist = you_dist + san_dist
            print("tot_dist", tot_dist)
            exit()
