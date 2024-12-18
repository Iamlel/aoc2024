from itertools import combinations
import re

tokensPattern = re.compile(r"[a-zA-Z\d]")

part1, part2 = set(), 0
with open("inputs/input8.txt", 'r') as f:
    l = f.readline()
    tokens = {}
    for y, line in enumerate([l] + f.readlines()):
        for token in tokensPattern.finditer(line):
            if (token.group() in tokens):
                tokens[token.group()].append((token.start(), y))
            else:
                tokens[token.group()] = [(token.start(), y)]
    mx, my = len(l) - 1, y + 1

    slopes = set()
    for tokenLocs in tokens.values():
        for p1, p2 in combinations(tokenLocs, 2):
            dx, dy = p1[0] - p2[0], p1[1] - p2[1]
            if (p1[0] + dx >= 0 and p1[1] + dy >= 0 and p1[0] + dx < mx and p1[1] + dy < my):
                part1.add((p1[0] + dx, p1[1] + dy))
            if (p2[0] - dx >= 0 and p2[1] - dy >= 0 and p2[0] - dx < mx and p2[1] - dy < my):
                part1.add((p2[0] - dx, p2[1] - dy))
            slopes.add((p1[0], p1[1], dy / dx))
    
    for x in range(mx):
        for y in range(my):
            for dx, dy, m in slopes:
                if (m * (x - dx) + dy == y):
                    part2 += 1
                    break
                
print(f"Part1: {len(part1)}")
print(f"Part2: {part2}")