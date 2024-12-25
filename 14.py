import re, math
from itertools import count

MAX_X, MAX_Y = 101, 103
SECONDS = 100

def findChristmasTree(robots, velocities):
    tree = []
    with open("inputs/tree.txt", 'r') as f:
        for y, line in enumerate(f.readlines()):
            for x, ch in enumerate(line):
                if (ch == '#'):
                    tree.append((x, y))
    tree.pop(0)

    for s in count(1):
        for i in range(len(robots)):
            robots[i] = ((robots[i][0] + velocities[i][0]) % MAX_X, (robots[i][1] + velocities[i][1]) % MAX_Y)
    
        for rx, ry in robots:   
            for tx, ty in tree:
                if (not (rx + tx, ry + ty) in robots):
                    break
            else:
                return s

part1 = [0] * 4
robots, velocities = [], []
with open("inputs/input14.txt", 'r') as f:
    midx, midy = (MAX_X >> 1), (MAX_Y >> 1)
    for line in f.readlines():
        x, y, vx, vy = [int(i) for i in re.findall("-?\d+", line)]

        robots.append((x, y))
        velocities.append((vx, vy))

        xf, yf = (vx * SECONDS + x) % MAX_X, (vy * SECONDS + y) % MAX_Y
        if (xf != midx and yf != midy):
            part1[(xf > midx) + 2 * (yf > midy)] += 1

print(f"Part1: {math.prod(part1)}")
print(f"Part2: {findChristmasTree(robots, velocities)}")