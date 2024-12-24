from collections import deque

part1, part2 = 0, 0
with open("inputs/input12.txt", 'r') as f:
    plots = set()
    for y, line in enumerate(f.readlines()):
        for x, ch in enumerate(line.strip()):
            plots.add((x, y, ch))

    stack, sidePoints = deque(), set()
    while (len(plots) > 0):
        visited = set()
        stack.append(plots.pop())
        perimeter = 0
        while (len(stack) > 0):
            current = stack.pop()

            visited.add(current)
            for ds, (dx, dy) in enumerate(((0, 1), (0, -1), (1, 0), (-1, 0))):
                new = (current[0] + dx, current[1] + dy, current[2])
                if (new in plots):
                    plots.remove(new)
                    visited.add(new)
                    stack.append(new)

                elif (not new in visited):
                    sidePoints.add((new[0], new[1], ds))
                    perimeter += 1

        sides = 0
        while (len(sidePoints) > 0):
            stack.append(sidePoints.pop())
            while (len(stack) > 0):
                current = stack.pop()
                for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    new = (current[0] + dx, current[1] + dy, current[2])
                    if (new in sidePoints):
                        sidePoints.remove(new)
                        stack.append(new)
            sides += 1
        part1 += len(visited) * perimeter
        part2 += len(visited) * sides

print(f"Part1: {part1}")
print(f"Part2: {part2}")