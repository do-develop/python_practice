"""
Until the remainder becomes 1
"""

# Get number and divider
num, div = map(int, input().split())
operation_count = 0

# if num is >= div keep divide by div
while num >= div:
    while num % div != 0:
        num -= 1
        operation_count += 1
    num //= div
    operation_count += 1

while num > 1:
    num -= 1
    operation_count += 1

print(operation_count)

