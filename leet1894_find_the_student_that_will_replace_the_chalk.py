class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        rem = k % total
        for i in range(len(chalk)):
            if rem >= chalk[i]:
                rem -= chalk[i]
            else:
                return i
        return -1
