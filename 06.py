movements = ((0, -1), (1, 0), (0, 1), (-1, 0))
graph = []
part1, part2 = set(), 0
with open("inputs/input6.txt", 'r') as f:
    for y, line in enumerate(f.readlines()):
        graph.append(list(line))
        if ('^' in line):
            guardx, guardy = line.index('^'), y
    graph[guardy][guardx] = '.'

    i = 0
    guardx2, guardy2 = guardx, guardy
    while (guardx > 0 and guardx < len(graph[0]) - 1 and guardy > 0 and guardy < len(graph) - 1):
        if (graph[guardy + movements[i][1]][guardx + movements[i][0]] == '#'):
            i = (i + 1) % 4
            continue
        guardx += movements[i][0]
        guardy += movements[i][1]
        part1.add((guardx, guardy))

    if ((guardx2, guardy2) in part1):
        part1.remove((guardx2, guardy2))

    for obsx, obsy in part1:
        i = 0
        visited = set()
        guardx, guardy = guardx2, guardy2
        while (guardx > 0 and guardx < len(graph[0]) - 1 and guardy > 0 and guardy < len(graph) - 1):
            if (graph[guardy + movements[i][1]][guardx + movements[i][0]] == '#' or (guardx + movements[i][0] == obsx and guardy + movements[i][1] == obsy)):
                i = (i + 1) % 4
                continue
            if ((guardx, guardy, i) in visited):
                part2 += 1
                break
            else:
                visited.add((guardx, guardy, i))
            guardx += movements[i][0]
            guardy += movements[i][1]

print(f"Part1: {len(part1) + 1}")
print(f"Part2: {part2}")
