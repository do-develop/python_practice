"""
Suppose we have two lists, weights and values of same length and another value capacity.
The weights[i] and values[i] represent the weight and value of ith element. So if we can
take at most capacity weights, and that we can take a fraction of an item's weight with
proportionate value, we have to find the maximum amount of value we can get (rounded down
to the nearest integer)
"""

from typing import List

class Solution:
    def get_max_value(self, weights: List[int], values: List[int], capacity: int) -> int:
        result = 0
        for pair in sorted(zip(weights, values), key=lambda x: - x[1]/x[0]):
            if not bool(capacity):
                break
            if pair[0] > capacity:
                result += pair[1] / (pair[0]/capacity)
                capacity = 0
            elif pair[0] <= capacity:
                result += pair[1]
                capacity -= pair[0]
        return result


values = [3, 5, 1, 2, 4]
weights = [40, 50, 20, 10, 30]
capacity = 75
print(Solution().get_max_value(weights, values, capacity))