# get number input as str
number = input()
count0 = 0  # case 1 - changing all numbers to 0
count1 = 0  # case 2 - changing all numbers to 1

if number[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(number) - 1):
    if number[i] != number[i + 1]:
        if number[i + 1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

"""
input: 0001100
output: 1
"""