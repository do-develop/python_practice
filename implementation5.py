number = input()
length = len(number)
total = 0

# left half sum
for i in range(length // 2):
    total += int(number[i])

# right half sum
for i in range(length//2, length):
    total -= int(number[i])

if total == 0:
    print("Lucky")
else:
    print("Ready")

# Test data: 123402
# Expected result: Lucky
