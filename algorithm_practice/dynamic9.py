count = int(input())

ugly = [0] * count
ugly[0] = 1

# index
i2 = i3 = i5 = 0
# multiply value
n2, n3, n5 = 2, 3, 5

for i in range(1, count):
    ugly[i] = min(n2, n3, n5)

    if ugly[i] == n2:
        i2 += 1
        n2 = ugly[i2] * 2
    if ugly[i] == n3:
        i3 += 1
        n3 = ugly[i3] * 3
    if ugly[i] == n5:
        i5 += 1
        n5 = ugly[i5] * 5

print(ugly[count - 1])
