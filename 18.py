from itertools import islice
import heapq
import re

END = (70, 70)
CORRUPTED_AMOUNT = 1024

def astar(corrupted, start, end):
    open = [(0, start[0], start[1])]
    closed = {start: 0}
    path = {}
    while (len(open) > 0):
        current = heapq.heappop(open)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next = (current[1] + dx, current[2] + dy)
            if (next[0] < 0 or next[0] > end[0] or next[1] < 0 or next[1] > end[1]):
                continue

            if (next in corrupted or next in closed):
                continue

            closed[next] = closed[(current[1], current[2])] + 1
            if (next == end):
                c = (current[1], current[2])
                parents = []
                while (c != start):
                    parents.append(c)
                    c = path[c]
                return (closed[next], parents)
            heapq.heappush(open, (closed[next] + abs(end[0] - next[0]) + abs(end[1] - next[1]), next[0], next[1]))
            path[next] = (current[1], current[2])
    return False, path

corrupted = set()
with open("inputs/input18.txt", 'r') as f:
    all_corrupted = iter(re.findall(r"(\d+),(\d+)", f.read()))
    for x, y in islice(all_corrupted, CORRUPTED_AMOUNT):
        corrupted.add((int(x), int(y)))

steps, path = astar(corrupted, (0, 0), END)
for x, y in all_corrupted:
    new = (int(x), int(y))
    corrupted.add(new)
    if (new in path):
        status, path = astar(corrupted, (0, 0), END)
        if (not status):
            break

print(f"Part1: {steps}")
print(f"Part2: {x},{y}")