import sys
import itertools
from time import sleep
from pyhelpers import Parser

def make_data(input_file):
    with open(input_file, "r") as f:
        return f.read().rstrip().split(",")

if len(sys.argv) > 1:
    print("INPUT\n")
    data = make_data("input")
else:
    print("EXAMPLE\n")
    data = make_data("example")

# -----------------

class Machine:
    def __init__(self, phase, data):
        self.phase = phase
        self.data = data
        self.pc = 0

    def run(self, inp):
        while True:
            instr = self.data[self.pc]
            instr = instr.zfill(5)
            opcode = instr[-2:]

            if opcode == "01":
                # print("ADD")
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                if mode1 == "0":
                    d1 = self.data[int(self.data[self.pc+1])]
                elif mode1 == "1":
                    d1 = self.data[self.pc+1]

                if mode2 == "0":
                    d2 = self.data[int(self.data[self.pc+2])]
                elif mode2 == "1":
                    d2 = self.data[self.pc+2]

                #print(f"{d1} + {d2} -> {int(self.data[self.pc+3])}")

                self.data[int(self.data[self.pc+3])] = str(int(d1) + int(d2))

                self.pc += 4
            elif opcode == "02":
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                if mode1 == "0":
                    d1 = self.data[int(self.data[self.pc+1])]
                elif mode1 == "1":
                    d1 = self.data[self.pc+1]

                if mode2 == "0":
                    d2 = self.data[int(self.data[self.pc+2])]
                elif mode2 == "1":
                    d2 = self.data[self.pc+2]

                # print(f"{d1} * {d2} -> {int(self.data[self.pc+3])}")

                self.data[int(self.data[self.pc+3])] = str(int(d1) * int(d2))

                self.pc += 4
            elif opcode == "03":
                if self.phase is not None:
                    self.data[int(self.data[self.pc+1])] = self.phase
                    self.phase = None
                else:
                    self.data[int(self.data[self.pc+1])] = inp
                self.pc += 2
            elif opcode == "04":
                mode = instr[-3:-2]
                if mode == "0":
                    d = self.data[int(self.data[self.pc+1])]
                elif mode == "1":
                    d = self.data[self.pc+1]
                print("OUT: ", d)
                self.pc += 2
                return int(d)
            elif opcode == "05":
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                if mode1 == "0":
                    d1 = self.data[int(self.data[self.pc+1])]
                elif mode1 == "1":
                    d1 = self.data[self.pc+1]

                if mode2 == "0":
                    d2 = self.data[int(self.data[self.pc+2])]
                elif mode2 == "1":
                    d2 = self.data[self.pc+2]

                if int(d1) != 0:
                    self.pc = int(d2)
                else:
                    self.pc += 3
            elif opcode == "06":
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                if mode1 == "0":
                    d1 = self.data[int(self.data[self.pc+1])]
                elif mode1 == "1":
                    d1 = self.data[self.pc+1]

                if mode2 == "0":
                    d2 = self.data[int(self.data[self.pc+2])]
                elif mode2 == "1":
                    d2 = self.data[self.pc+2]

                if int(d1) == 0:
                    self.pc = int(d2)
                else:
                    self.pc += 3
            elif opcode == "07":
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                if mode1 == "0":
                    d1 = self.data[int(self.data[self.pc+1])]
                elif mode1 == "1":
                    d1 = self.data[self.pc+1]

                if mode2 == "0":
                    d2 = self.data[int(self.data[self.pc+2])]
                elif mode2 == "1":
                    d2 = self.data[self.pc+2]

                if int(d1) < int(d2):
                    self.data[int(self.data[self.pc+3])] = 1
                else:
                    self.data[int(self.data[self.pc+3])] = 0

                self.pc += 4
            elif opcode == "08":
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                if mode1 == "0":
                    d1 = self.data[int(self.data[self.pc+1])]
                elif mode1 == "1":
                    d1 = self.data[self.pc+1]

                if mode2 == "0":
                    d2 = self.data[int(self.data[self.pc+2])]
                elif mode2 == "1":
                    d2 = self.data[self.pc+2]

                if int(d1) == int(d2):
                    self.data[int(self.data[self.pc+3])] = 1
                else:
                    self.data[int(self.data[self.pc+3])] = 0

                self.pc += 4
            elif opcode == "99":
                print("HALT")
                return None

n_machines = 5

phases = itertools.permutations('56789', 5)

best_phase = ""
best_output = 0

for phase in phases:
    machines = [Machine(int(x), data.copy()) for x in phase]

    inp = 0

    last_out = 0
    while True:
        for n in range(0, len(machines)):
            inp = machines[n].run(inp)
            if inp is None:
                break
        if inp is None:
            break
        last_out = inp

    if last_out > best_output:
        best_output = last_out
        best_phase = phase

print("BEST:", best_phase, best_output)
