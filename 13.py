import re, numpy

def is_whole(n):
    return n % 1 == 0

part1, part2 = 0, 0
with open("inputs/input13.txt", 'r') as f:
    for machine in f.read().split("\n\n"):
        x1, y1, x2, y2, x, y = [int(m) for m in re.findall("\d+", machine)]
        for q2 in reversed(range(min(x // x2, y // y2, 99) + 1)):
            q1, mx = divmod(x - x2 * q2, x1)
            q1y, my = divmod(y - y2 * q2, y1)
            if (mx + my == 0 and q1 - q1y == 0 and q1 <= 100):
                part1 += 3 * q1 + q2
                break

        q1, q2 = numpy.linalg.solve(numpy.array([[x1, x2], [y1, y2]]), numpy.array([x+10000000000000, y+10000000000000]))
        if (abs(q1 - round(q1)) <= 0.001):
            part2 += 3 * round(q1) + round(q2)
print(f"Part1: {part1}")
print(f"Part2: {part2}")