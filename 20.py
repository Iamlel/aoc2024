from itertools import combinations
import heapq

def manhattan_distance(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def astar(barriers, start, end):
    open = [(0, start[0], start[1])]
    closed = {start: 0}
    path = {}
    while (len(open) > 0):
        current = heapq.heappop(open)
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            next = (current[1] + dx, current[2] + dy)
            if (next in barriers or next in closed):
                continue

            closed[next] = closed[(current[1], current[2])] + 1
            if (next == end):
                c = (current[1], current[2])
                parents = []
                while (c != start):
                    parents.append(c)
                    c = path[c]
                return [end] + parents + [start]
            heapq.heappush(open, (closed[next] + manhattan_distance(next, end), next[0], next[1]))
            path[next] = (current[1], current[2])
    return False

start, end = (0, 0), (0, 0)
barriers = set()
with open("inputs/input20.txt", 'r') as f:
    for y, line in enumerate(f.readlines()):
        for x, ch in enumerate(line.strip()):
            match (ch):
                case 'S':
                    start = (x, y)
                case 'E':
                    end = (x, y)
                case '#':
                    barriers.add((x, y))

part1, part2 = 0, 0
# could be faster if we stored the manhattan distance in the path, instead of calculating twice
for (x, p1), (y, p2) in combinations(enumerate(astar(barriers, start, end)), 2): # x > y
    d = manhattan_distance(p1, p2)
    if (y - x - d >= 100):
        part1 += (d == 2)
        part2 += (d <= 20)

print(f"Part1: {part1}")
print(f"Part2: {part2}")