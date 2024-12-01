import bisect

nums1, nums2 = [], []
with open("input.txt", "r") as f:
    for num1, num2 in f.readlines().split("   "):
        new_line = line.split("   ")
        bisect.insort(nums1, int(new_line[0]))
        bisect.insort(nums2, int(new_line[1]))

part1 = 0
for x in range(len(num1)):
    part1 += abs(num1[x] - num2[x])

print("Part1: " + part1)
print("Part2: " + sum([num * num2.count(num) for num in num1]))
