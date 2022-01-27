# 2xn tile problem

width = int(input())

# initialise DP table
d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, width + 1):
    d[i] = d[i-1] + d[i-2] * 2

print(d[width])