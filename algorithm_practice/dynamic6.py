size = int(input())
dp = []

for _ in range(size):
    dp.append(list(map(int, input().split())))

for r in range(1, size):
    for c in range(r + 1):
        if c == 0:
            up_left = 0
        else:
            up_left = dp[r-1][c-1]
        if c == r:
            up = 0
        else:
            up = dp[r-1][c]

        dp[r][c] = dp[r][c] + max(up_left, up)

print(max(dp[size -1]))
