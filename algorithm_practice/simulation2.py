from itertools import combinations

city_size, branch_count = map(int, input().split())
branch, house = [], []

for r in range(city_size):
    row  = list(map(int, input().split()))
    for c in range(city_size):
        if row[c] == 1:
            house.append((r,c))
        elif row[c] == 2:
            branch.append((r,c))

candidates = list(combinations(branch, branch_count))

def get_distance(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx-cx) + abs(hy-cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_distance(candidate))

print(result)


