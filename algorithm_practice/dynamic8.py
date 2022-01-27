count = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1] * count

for i in range (1, count):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(count - max(dp))
