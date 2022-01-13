count = int(input())
t = [] # time to complete
m = [] # money upon completion
dp = [0] * (count + 1)
max_value = 0

for _ in range(count):
    x,y = map(int, input().split())
    t.append(x)
    m.append(y)

for i in range(count-1, -1, -1):
    time = t[i] + i

    if time <= count:
        dp[i] = max(m[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)
    
