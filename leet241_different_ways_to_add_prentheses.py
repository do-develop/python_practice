"""
Given a string expression of numbers and operators, return all possible
results from computing all the different possible ways to group numbers
and operators. You may return the answer in any order.
"""
from typing import List

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        if expression.isdigit():
            return [int(expression)]

        results = []
        for index, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index+1:])

                results.extend(compute(left, right, value))

        return results
# Test
expression = "2*3-4*5"
print(Solution().diffWaysToCompute(expression))