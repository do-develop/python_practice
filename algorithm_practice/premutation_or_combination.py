"""
import itertools

data = [1, 2, 3]

# permutations
print("Permutations")
for x in itertools.permutations(data, 2):
    print(list(x), end = ' ')
# combinations
print()
print("Combinations")
for x in itertools.combinations(data, 2):
    print(list(x), end = ' ')
"""

from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
pass_size, cand_size = map(int, input().split(' '))

candidates = input().split(' ')
candidates.sort()

for password in combinations(candidates, pass_size):
    count = 0
    for i in password:
        if i in vowels:
            count += 1

    if count >= 1 and count <= pass_size - 2:
        print(''.join(password))
