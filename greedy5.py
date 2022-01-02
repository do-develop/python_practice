# get number input as str
number = input()
result = int(number[0])

for i in range(1, len(number)):
    num = int(number[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)

"""
input: 02984
output: 576
"""