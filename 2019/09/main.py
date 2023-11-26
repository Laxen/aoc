import sys
import numpy as np
from pyhelpers import Parser

np.set_printoptions(linewidth=np.inf)

def make_data(input_file):
    with open(input_file, "r") as f:
        return f.readline().rstrip().split(",")

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
        self.base = 0
        self.out = ""

        self.data += ["0" for _ in range(10000000)]

    def _get_param(self, mode, pc):
        ret = None
        if mode == "0":
            ret = self.data[int(self.data[pc])]
            print("mode 0:", ret)
        elif mode == "1":
            ret = self.data[pc]
            print("mode 1:", ret)
        elif mode == "2":
            ret = self.data[self.base + int(self.data[pc])]
            print("mode 2:", ret)
        return ret

    def run(self, inp):
        while True:
            instr = self.data[self.pc]
            instr = instr.zfill(5)
            opcode = instr[-2:]

            print("instr:", instr)

            if opcode == "01":
                # print("ADD")
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                d1 = self._get_param(mode1, self.pc+1)
                d2 = self._get_param(mode2, self.pc+2)

                self.data[int(self.data[self.pc+3])] = str(int(d1) + int(d2))

                self.pc += 4
            elif opcode == "02":
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                d1 = self._get_param(mode1, self.pc+1)
                d2 = self._get_param(mode2, self.pc+2)

                store = int(self.data[self.pc+3])
                self.data[store] = str(int(d1) * int(d2))

                self.pc += 4

                print(f"*{store} = {d1} * {d2} = {self.data[store]}")
            elif opcode == "03":
                mode = instr[-3:-2]

                d = self._get_param(mode, self.pc+1)

                if self.phase is not None:
                    self.data[int(d)] = str(self.phase)
                    self.phase = None
                else:
                    self.data[int(d)] = str(inp)
                self.pc += 2
            elif opcode == "04":
                mode = instr[-3:-2]

                d = self._get_param(mode, self.pc+1)

                print("OUT: ", d)
                self.pc += 2
                self.out += f", {d}"
                return int(d)
            elif opcode == "05":
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                d1 = self._get_param(mode1, self.pc+1)
                d2 = self._get_param(mode2, self.pc+2)

                if int(d1) != 0:
                    self.pc = int(d2)
                    print(f"{d1} != 0, pc = {self.pc}")
                else:
                    self.pc += 3
                    print(f"{d1} == 0, pc = {self.pc}")
            elif opcode == "06":
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                d1 = self._get_param(mode1, self.pc+1)
                d2 = self._get_param(mode2, self.pc+2)

                if int(d1) == 0:
                    print(d1, "== 0, jmp", d2)
                    self.pc = int(d2)
                else:
                    print(d1, "!= 0, cont")
                    self.pc += 3
            elif opcode == "07":
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                d1 = self._get_param(mode1, self.pc+1)
                d2 = self._get_param(mode2, self.pc+2)

                store = int(self.data[self.pc+3])
                if int(d1) < int(d2):
                    self.data[store] = str(1)
                else:
                    self.data[store] = str(0)

                print(f"*{store} = {d1} < {d2} = {self.data[store]}")
                self.pc += 4
            elif opcode == "08":
                mode1 = instr[-3:-2]
                mode2 = instr[-4:-3]

                d1 = self._get_param(mode1, self.pc+1)
                d2 = self._get_param(mode2, self.pc+2)

                if int(d1) == int(d2):
                    self.data[int(self.data[self.pc+3])] = str(1)
                else:
                    self.data[int(self.data[self.pc+3])] = str(0)

                self.pc += 4
            elif opcode == "09":
                self.base += int(self.data[self.pc+1])
                self.pc += 2
                print("base set to", self.base)
            elif opcode == "99":
                print("HALT")
                print("Complete output:", self.out)
                return None
            else:
                print("Unknown opcode:", opcode, "program:", self.data[0:20], "base:", self.base)
                return None

m = Machine(None, data)
while m.run(1) != None:
    pass
