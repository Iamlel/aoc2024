from collections import deque
import math

def prepareValues(line):
    goal, values = line.split(": ")
    return int(goal), [int(v) for v in values.split(' ')]
    
def calibrate(goal, values, newOp):
    options = deque()
    options.append(values.pop(0))
    for value in values:
        for _ in range(len(options)):
            option = options.popleft()
            newOption1, newOption2 = option * value, option + value
            if (newOp):
                if (value != 0):
                    newOption3 = option * 10 ** (math.floor(math.log10(value)) + 1) + value
                else:
                    newOption3 = option * 10 + option

                if (newOption3 <= goal):
                    options.append(newOption3)
            
            if (newOption1 <= goal):
                options.append(newOption1)

            if (newOption2 <= goal):
                options.append(newOption2)
    return (any(o == goal for o in options))

part1, part2 = 0, 0
with open("inputs/input7.txt", 'r') as f:
    for line in f.readlines():
        goal, values = prepareValues(line)
        if (calibrate(goal, values.copy(), False)):
            part1 += goal

        elif calibrate(goal, values, True):
            part2 += goal

print(f"Part1: {part1}")
print(f"Part2: {(part1 + part2)}")