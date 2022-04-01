"""
You have observations of n + m 6-sided dice rolls with each face numbered from
1 to 6. n of the observations went missing, and you only have the observations
of m rolls. Fortunately, you have also calculated the average value of the n +
m rolls.

You are given an integer array rolls of length m where rolls[i] is the value of
the ith observation. You are also given the two integers mean and n.

Return an array of length n containing the missing observations such that the
average value of the n + m rolls is exactly mean. If there are multiple valid
answers, return any of them. If no such array exists, return an empty array.

The average value of a set of k numbers is the sum of the numbers divided by k.

Note that mean is an integer, so the sum of the n + m rolls should be divisible
by n + m.
"""
# Solution Approach: Greedy Algorithm
from typing import List

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        nTotal = (mean * (n + m)) - sum(rolls)

        if nTotal < n or nTotal > n*6 :
            return []

        result = []
        while nTotal:
            dice = min(nTotal - n + 1, 6)
            result.append(dice)
            nTotal -= dice
            n -= 1

        return result


# TEST
rolls = [3,2,4,3]
mean = 4
n = 2
print(Solution().missingRolls(rolls, mean, n))
# Output: [6,6]
# Explanation: The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
