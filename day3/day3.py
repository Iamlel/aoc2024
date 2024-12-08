import re

pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")

part1, part2 = 0, 0
with open("input.txt", "r") as f:
    text = f.read()
    part1 = sum([int(a) * int(b) for a, b in pattern.findall(text)])
    for invalid in text.split("don't()"):
        part2 += sum([int(a) * int(b) for a, b in pattern.findall(invalid[:invalid.find("do()")])])

print(f"Part1: {part1}")
print(f"Part2: {part1 - part2}")
