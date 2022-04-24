"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to
wait after the ith day to get a warmer temperature. If there is no future day
for which this is possible, keep answer[i] == 0 instead.
"""
from typing import List

# Solution approach - monotonic stack (monotonic decreasing order)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []  # pair: [temperature, index of temperature]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_temp, stack_idx = stack.pop()
                result[stack_idx] = (i - stack_idx)
            stack.append([t, i])
        return result
        
        




# TEST
temperatures = [73,74,75,71,69,72,76,73]
print(Solution().dailyTemperatures(temperatures))
# expected output: [1,1,4,2,1,1,0,0]
