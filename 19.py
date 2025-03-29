def arrange(request, patterns, cache):
    total = 0
    for p in patterns:
        if (request in cache):
            return cache[request]
        
        if (request == p):
            total += 1
        
        elif (request.startswith(p)):
            total += arrange(request[request.index(p) + len(p):], patterns, cache)

    cache[request] = total
    return total

with open("inputs/input19.txt", 'r') as f:
    p, requests = f.read().split("\n\n")
    patterns = p.split(", ")

arrangements = [arrange(r, patterns, {}) for r in requests.splitlines()]

print(f"Part1: {len(arrangements) - arrangements.count(0)}")
print(f"Part2: {sum(arrangements)}")