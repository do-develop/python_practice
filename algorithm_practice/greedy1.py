# Get N, M, K (array size, add count, max count for same number used for addition)
n, m, k = map(int, input().split())
# Get numbers in a list
numbers = list(map(int, input().split()))

# Sort the input data
numbers.sort()
first_big, second_big = numbers[n - 1], numbers[n - 2]

# count the total add_count of the biggest number
count = int(m / (k + 1)) * k
count += m % (k + 1)

result = 0
result += (count * first_big)
result += (m - count) * second_big

print(result)
"""
5 8 3 
2 4 5 4 6
46  # result
"""
