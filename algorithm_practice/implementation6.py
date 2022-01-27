data = input()
result = []
value, value_count = 0, 0

for c in data:
    if c.isalpha():
        result.append(c)
    else:
        value += int(c)
        value_count += 1

result.sort()

if value_count != 0:
    result.append(str(value))

print(''.join(result))
