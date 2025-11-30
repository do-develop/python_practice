class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        positions, occurences = [], []

        for i, num in enumerate(nums):
            if num == x:
                positions.append(i)

        for q in queries:
            if len(positions) < q:
                occurences.append(-1)
            else:
                occurences.append(positions[q-1])
        
        return occurences