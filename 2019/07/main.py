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

def handle_instr(instr):
    global pc, data, inp

    instr = instr.zfill(5)
    opcode = instr[-2:]

    if opcode == "01":
        # print("ADD")
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        #print(f"{d1} + {d2} -> {int(data[pc+3])}")

        data[int(data[pc+3])] = str(int(d1) + int(d2))

        pc += 4
    elif opcode == "02":
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        # print(f"{d1} * {d2} -> {int(data[pc+3])}")

        data[int(data[pc+3])] = str(int(d1) * int(d2))

        pc += 4
    elif opcode == "03":
        data[int(data[pc+1])] = inp.pop(0)
        pc += 2
    elif opcode == "04":
        mode = instr[-3:-2]
        if mode == "0":
            d = data[int(data[pc+1])]
        elif mode == "1":
            d = data[pc+1]
        print("OUT: ", d)
        inp.insert(1, int(d))
        pc += 2
    elif opcode == "05":
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        if int(d1) != 0:
            pc = int(d2)
        else:
            pc += 3
    elif opcode == "06":
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        if int(d1) == 0:
            pc = int(d2)
        else:
            pc += 3
    elif opcode == "07":
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        if int(d1) < int(d2):
            data[int(data[pc+3])] = 1
        else:
            data[int(data[pc+3])] = 0

        pc += 4
    elif opcode == "08":
        mode1 = instr[-3:-2]
        mode2 = instr[-4:-3]

        if mode1 == "0":
            d1 = data[int(data[pc+1])]
        elif mode1 == "1":
            d1 = data[pc+1]

        if mode2 == "0":
            d2 = data[int(data[pc+2])]
        elif mode2 == "1":
            d2 = data[pc+2]

        if int(d1) == int(d2):
            data[int(data[pc+3])] = 1
        else:
            data[int(data[pc+3])] = 0

        pc += 4
    elif opcode == "99":
        return False
    return True


orig_data = data.copy()
n_machines = 5

# All numbers with n_machines digits, as integer
phases = itertools.permutations('01234', 5)

best_phase = ""
best_output = 0

for phase in phases:
    inp = [int(x) for x in phase]
    inp.insert(1, 0)
    for n in range(0, n_machines):
        data = orig_data.copy()
        pc = 0

        while pc < len(data):
            instr = data[pc]
            ret = handle_instr(instr)
            if not ret:
                if inp[0] > best_output:
                    print("output:", inp[0])
                    best_output = inp[0]
                    best_phase = phase
                break

print("BEST:", best_phase, best_output)
