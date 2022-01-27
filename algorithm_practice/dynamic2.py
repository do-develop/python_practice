house = list(map(int, input().split()))
count = len(house)

cur, prev = 0, 0

for money in house:
    temp = max(cur, money + prev)
    prev = cur
    cur = temp

print(cur)