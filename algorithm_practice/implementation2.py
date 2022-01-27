# get hour
hour = int(input())

count_3 = 0
for h in range (hour + 1):
    for m in range (60):
        for s in range(60):
            if '3' in str(h) + str(m) + str(s):
                count_3 += 1

print(count_3)
"""
3 
result = 11475
"""