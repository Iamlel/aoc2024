from collections import deque
import re

def parseProgram(program):
    return [int(v) for v in re.findall(r"\d", program)]

def combo(registers, operand):
    INT_REG = ['A', 'B', 'C']

    if (operand == 7):
        raise ValueError("Operand 7 is reserved and invalid.")
    elif (operand > 3):
        return registers[INT_REG[operand - 4]]
    else:
        return operand

def adv(registers, operand):
    return registers['A'] >> combo(registers, operand)

def execute(registers, program):
    ptr = 0
    while (ptr < len(program)):
        opcode, operand = program[ptr], program[ptr+1]
        match (opcode):
            case 0:
                registers['A'] = adv(registers, operand)
            case 1:
                registers['B'] ^= operand
            case 2:
                registers['B'] = combo(registers, operand) % 8
            case 3 if (registers['A'] != 0):
                ptr = operand - 2
            case 4:
                registers['B'] ^= registers['C']
            case 5:
                yield str(combo(registers, operand) % 8)
            case 6:
                registers['B'] = adv(registers, operand)
            case 7:
                registers['C'] = adv(registers, operand)
        ptr += 2

registers = {'A': 0, 'B': 0, 'C': 0}
program = []
with open("inputs/input17.txt", 'r') as f:
    reg, program = f.read().split("\n\n")
    registers.update({k: int(v) for k, v in re.findall(r"([A-C]): (\d+)", reg)})
    program = parseProgram(program)

possibilities = deque([0])
for expected in reversed(program):
    for _ in range(len(possibilities)):
        y = possibilities.popleft()
        possibilities.extend(y * 8 + r for r in range(8) if (int(next(execute({'A': y * 8 + r}, program))) == expected))

print(f"Part1: {','.join(execute(registers, program))}")
print(f"Part2: {min(possibilities)}")