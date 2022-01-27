# Get sectional sum using prefix sum

data = [10, 20, 30, 40, 50]
data_size = len(data)

# calculate prefix_sum
total = 0
prefix_sum = [0]
for i in data:
    total += i
    prefix_sum.append(total)

# get sectional sum (position 3 to 4)
l, r = 3, 4
print(prefix_sum[r] - prefix_sum[l - 1])
