num_count = int(input())
numbers = list(map(int, input().split()))
# get operator counts
add, sub, mul, div = map(int, input().split())

# initialise min and max value
min_val = 1e9
max_val = -1e9

# DFS
def dfs(i, now):
    global min_val, max_val, add, sub, mul, div
    # if used all operators then update min and max val
    if i == num_count:
        min_val = min(min_val, now)
        max_val = max(max_val, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / numbers[i]))
            div += 1

dfs(1, numbers[0])

print(max_val)
print(min_val)
               
