"""
Given an integer numRows, return the first numRows of Pascal's triangle. In
Pascal's triangle, each number is the sum of the two numbers directly above it
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]

        for i in range(numRows - 1):
            temp = [0] + rows[-1] + [0]
            new_row = []
            for j in range(len(rows[-1]) + 1):
                new_row.append(temp[j] + temp[j+1])
            rows.append(new_row)
        return rows
        
        




if __name__ == "__main__":
    numRows = 5
    print(Solution().generate(numRows))
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
