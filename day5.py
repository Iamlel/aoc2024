from itertools import combinations, permutations

# O(C(n ,2))
# could have been O(n)
# if I actually made the graph
# sort itself into a tree
def checkOrder(orderGroup, graph):
    for small, big in combinations(orderGroup, 2):
        if (not small in graph or not big in graph[small]):
            return False
    return True

def generatePermutation(orderGroup, graph):
    permutation = []
    for order in orderGroup:
        if (not order in graph):
            permutation.append(order)

        else:
            permutation.insert(next((i for i, o in enumerate(permutation) if o in graph[order]), len(permutation)), order)
    return permutation

def middleNumber(orderGroup):
    return int(orderGroup[int(len(orderGroup) * 0.5)])

graph = {}
part1, part2 = 0, 0
with open("inputs/input5.txt", 'r') as f:
    instructions, orders = f.read().split("\n\n")
    for instruction in instructions.split('\n'):
        # small is top, big is bottom
        small, big = instruction.split('|')
        if (small in graph):
            graph[small].add(big)
        else:
            graph[small] = set([big])

    for order in orders.split('\n')[:-1]:
        orderGroup = order.split(',')
        if (checkOrder(orderGroup, graph)):
            part1 += middleNumber(orderGroup)
        else:
            part2 += middleNumber(generatePermutation(orderGroup, graph))

print(f"Part1: {part1}")
print(f"Part2: {part2}")
