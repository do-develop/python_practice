for tc in range(int(input())):
    row, col = map(int, input().split())
    array = list(map(int, input().split()))

dp = []
index = 0
for i in range(row):
    dp.append(array[index:index + col])
    index += col

for c in range(1, col):
    for r in range(row):
        if r == 0:
            left_up = 0
        else:
            left_up = dp[r-1][c-1]
        if r == row-1:
            left_down = 0
        else:
            left_down = dp[r+1][c-1]
        left = dp[r][c-1]
        dp[r][c] = dp[r][c] + max(left_up, left, left_down)

result = 0
for i in range(row):
    result = max(result, dp[i][col - 1])

print(result)
