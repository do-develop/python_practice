import collections
"""
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each character in stones is a type
of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

# Method 1 - using hash table
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = {}  # declare a hash table
        count = 0

        for char in stones:
            if char not in freqs:
                freqs[char] = 1
            else:
                freqs[char] += 1

        for char in jewels:
            if char in freqs:
                count += freqs[char]

        return count

# Method 2 - using defaultdict
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.defaultdict(int)
        count = 0

        for char in stones:
            freqs[char] += 1

        for char in jewels:
            count += freqs[char]

        return count

# Method 3 - using counter
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        freqs = collections.Counter(stones)
        count = 0

        for char in jewels:
            count += freqs[char]

        return count
        
"""

# Method 4 - Pythonic way
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(s in jewels for s in stones)

jewels = "aA"
stones = "aAAbbbb"

print(Solution().numJewelsInStones(jewels, stones))