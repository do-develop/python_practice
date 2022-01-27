ball_count, max_weight = map(int, input().split())
weights = list(map(int, input().split()))

count_per_weight = [0] * 11

for w in weights:
    count_per_weight[w] += 1

result = 0
for i in range(1, max_weight+1):
    ball_count -= count_per_weight[i]
    result += count_per_weight[i] * ball_count

print(result)

"""
5 3
1 3 2 3 2

8
"""