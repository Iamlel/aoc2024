from collections import deque
import math

def add_instructions(a: int, n: int, s: int):
    return n * (a * (2 * s + a - 1)) // 2

part1, part2 = 0, 0
with open("inputs/input9.txt", 'r') as f:
    instructions2 = [int(x) for x in f.read().strip()]

    if (not len(instructions2) % 2):
        instructions2.pop()
    instructions = deque(instructions2.copy())

    s = ptr = 0
    while (len(instructions) > 0):
        a = instructions.popleft()
        if (ptr % 2): # odd ptr                 
            while (instructions[-1] <= a):
                a2 = instructions.pop()
                a -= a2
                part1 += add_instructions(a2, len(instructions) // 2 + math.ceil(ptr * 0.5), s)
                s += a2
                instructions.pop() # skip the empty stuff
            part1 += add_instructions(a, len(instructions) // 2, s)
            instructions[-1] -= a
        part1 += add_instructions(a, math.ceil(ptr * 0.5), s)
        s += a
        ptr += 1

    e, holes = 0, []
    for ptr, a in enumerate(instructions2):
        if (ptr % 2):
            holes.append([a, e])
        e += a

    n = len(instructions2) // 2
    for ptr, a in enumerate(reversed(instructions2)):
        e -= a
        if (not ptr % 2):
            for x, (a2, s) in enumerate(holes):
                if (s > e):
                    holes.pop(x)
                    continue

                if (a2 > a):
                    part2 += add_instructions(a, n, s)
                    holes[x] = [a2 - a, s + a]
                    break

                elif (a2 == a):
                    part2 += add_instructions(a, n, holes.pop(x)[1])
                    break
            else:
                part2 += add_instructions(a, n, e)
            n -= 1

print(f"Part1: {part1}")
print(f"Part2: {part2}")