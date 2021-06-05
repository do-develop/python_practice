
# Given an array of integers, determine whether the array is monotonic or not.

A = [6, 5, 4, 8]
B = [1, 1, 2, 3, 3, 2, 1]
C = [1, 2, 3, 7, 8]
D = []

def check_monotonic(num_array):
    return (all(num_array[i] <= num_array[i+1] for i in range(len(num_array) - 1)) or
            all(num_array[i] >= num_array[i+1] for i in range(len(num_array) - 1)))

print(check_monotonic(A))
print(check_monotonic(B))
print(check_monotonic(C))
print(check_monotonic(D))