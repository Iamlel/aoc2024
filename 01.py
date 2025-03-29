import bisect

nums1, nums2 = [], []
with open("inputs/input1.txt", "r") as f:
    for line in f.readlines():
        num1, num2 = line.split("   ")
        bisect.insort(nums1, int(num1))
        bisect.insort(nums2, int(num2))

part1 = 0
for x in range(len(nums1)):
    part1 += abs(nums1[x] - nums2[x])

print(f"Part1: {part1}")
print(f"Part2: {sum([num * nums2.count(num) for num in nums1])}")
