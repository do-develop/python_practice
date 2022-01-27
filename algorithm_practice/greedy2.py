# Get row and column counts
r, c = map(int, input().split())

result = 0

for i in range(r):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)