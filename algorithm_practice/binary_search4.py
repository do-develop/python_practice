house, router = list(map(int, input().split(' ')))

# house coordinates
array = []
for _ in range(house):
    array.append(int(input()))
array.sort()

min_gap = 1
max_gap = array[-1] - array[0]
result = 0

while(min_gap <= max_gap):
    mid = (min_gap + max_gap) // 2
    value = array[0]
    count = 1
    # install router using mid_gap
    for i in range(1, house):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= router:
        min_gap = mid + 1
        result = mid
    else:
        max_gap = mid - 1

print(result)
