# get participants size
participant_size = int(input())
fear_level = list(map(int, input().split()))
fear_level.sort()

# result variable
group_count = 0
member_count = 0

for level in fear_level:
    member_count += 1
    if member_count >= level:
        group_count += 1
        member_count = 0  # reset for next group

print(group_count)

"""
input:
5
2 3 1 2 2
output:
2
"""