from collections import deque

part1, part2 = 0, 0 
with open("inputs/input10.txt", 'r') as f:
    graph, starts = [], []
    for y, line in enumerate(f.readlines()):
        for x, ch in enumerate(line.strip()):
            if (ch == '0'):
                starts.append((x, y))
        graph.append([int(ch) for ch in line.strip()])
    
    # Can use a hashmap to see if 2 paths intersect
    for start in starts:
        stack = deque([start])
        ends = set()
        while (len(stack) > 0):
            node = stack.pop()
            for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                if (node[0] + dx < 0 or node[1] + dy < 0 or node[0] + dx >= len(graph[0]) or node[1] + dy >= len(graph)):
                    continue

                if (graph[node[1] + dy][node[0] + dx] - graph[node[1]][node[0]] == 1):
                    if (graph[node[1] + dy][node[0] + dx] == 9):
                        ends.add((node[0] + dx, node[1] + dy))
                        part2 += 1
                    else:
                        stack.append((node[0] + dx, node[1] + dy))
        part1 += len(ends)
        
print(f"Part1: {part1}")
print(f"Part2: {part2}")