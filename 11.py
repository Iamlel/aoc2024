import math

def addStoneValue(stones, stone, value):
    if (stone in stones):
        stones[stone] += value
    else:
        stones[stone] = value

def blinkStones(stones, blinks):
    newStones = {}
    for stone in stones:
        if (stone == 0):
            addStoneValue(newStones, 1, stones[stone])
        else:
            digits = math.floor(math.log10(stone)) + 1
            if (not digits % 2):
                divisor = 10 ** (digits // 2)
                addStoneValue(newStones, stone % divisor, stones[stone])
                addStoneValue(newStones, stone // divisor, stones[stone])
            else:
                addStoneValue(newStones, stone * 2024, stones[stone])

    if (blinks - 1 == 0):
        return newStones
    else:
        return blinkStones(newStones, blinks - 1)

stones = {}
with open("inputs/input11.txt", 'r') as f:
    for stone in f.read().strip().split(" "):
        addStoneValue(stones, int(stone), 1)
    stones = blinkStones(stones, 25)
    
print(f"Part1: {sum(stones.values())}") # after 25
print(f"Part2: {sum(blinkStones(stones, 50).values())}") # after 25 and 50 more