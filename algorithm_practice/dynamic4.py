type_count, target_amount = map(int, input().split())
coin = []
for i in range(type_count):
    coin.append(int(input()))

d = [10001] * (target_amount + 1)
d[0] = 0

for i in range(type_count):
    for j in range(coin[i], target_amount + 1):
        if d[j - coin[i]] != 10001:
            d[j] = min(d[j], d[j - coin[i]]+1)

if d[target_amount] == 10001:
    print(-1)
else:
    print(d[target_amount])
