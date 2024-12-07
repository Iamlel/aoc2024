import numpy

def checkChanges(changes):
    direction = numpy.sign(changes[0])
    return not any((not change or change * change > 9 or direction != numpy.sign(change)) for change in changes)

def addAdjacentChanges(l):
    yield l[1:]
    for i in range(len(l) - 1):
        new = l.copy()
        p = new.pop(i)
        new[i] += p
        yield new
    yield l[:-1]

part1, part2 = 0, 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        levels = [int(level) for level in line.split(" ")]
        changes = [a - b for a, b in zip(levels[:-1], levels[1:])]

        if (checkChanges(changes)):
            part1 += 1

        if any(checkChanges(changes2) for changes2 in addAdjacentChanges(changes)):
            part2 += 1

print(f"Part1: {part1}")
print(f"Part2: {part2}")
