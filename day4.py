import numpy, re

def rotate90(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0])-1,-1,-1)]

def rotate45(l):
    ctr = 0
    new = []
    while(ctr < 2 * len(l) - 1):
        lst = []
        for i in range(len(l[0])):
            for j in range(len(l)):
                if i + j == ctr:
                    lst.append(l[i][j])

        lst.reverse()
        new.append(lst)
        ctr += 1
    return new

# ymax = len - 1
def rotate315(x, y, ymax):
    if (y <= ymax):
        return (x, y - x)
    else:
        return (x + y - ymax, ymax - x)

def rotate225(x, y, ymax):
    if (y <= ymax):
        return (ymax - y + x, x)
    else:
        return (x, y + x - ymax)

pattern = re.compile(r"(?<=M)AS|(?<=S)AM")
part1, part2 = 0, 0
with open("inputs/input4.txt", "r") as f:
    l = [[c for c in line.strip()] for line in f.readlines()]
    li = l.copy()

    part1 += sum(''.join(line).count("XMAS") + ''.join(line).count("SAMX") for line in li)

    locs = []
    for i, letters in enumerate(rotate45(li)):
        letterStr = ''.join(letters)
        part1 += letterStr.count("XMAS") + letterStr.count("SAMX")

        for j in pattern.finditer(letterStr):
            locs.append(rotate315(j.start(), i, len(li) - 1))

    li = rotate90(li)
    part1 += sum(''.join(line).count("XMAS") + ''.join(line).count("SAMX") for line in li)

    for i, letters in enumerate(rotate45(li)):
        letterStr = ''.join(letters)
        part1 += letterStr.count("XMAS") + letterStr.count("SAMX")

        for j in pattern.finditer(letterStr):
            part2 += (rotate225(j.start(), i, len(li) - 1) in locs)

print(f"Part1: {part1}")
print(f"Part2: {part2}")
