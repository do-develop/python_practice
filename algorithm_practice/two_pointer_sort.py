# Two already sorted arrays --> make one sorted array
a = [1,3,5]
b = [2,4,6,8]
a_size, b_size = len(a), len(b)

result = [0] * (a_size + b_size)

i, j, k = 0, 0, 0

while i < a_size or j < b_size:
    if j >= b_size or (i < a_size and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(result)
