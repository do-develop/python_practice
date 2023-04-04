class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        # Greedy approach
        count = 0 # column deletion count
        row, col = len(strs), len(strs[0])
        unsorted = set(range(row - 1))
        for c in range(col): 
            if any(strs[r][c] > strs[r + 1][c] for r in unsorted):
                count += 1
            else: # keep this column == remove from unsorted
                unsorted -= {r for r in unsorted if strs[r][c] < strs[r+1][c]}
        return count
