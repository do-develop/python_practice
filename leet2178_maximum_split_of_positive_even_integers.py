class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        final = finalSum
        ans, curr = [], 2

        if final % 2 == 0:
            while curr <= final:
                ans.append(curr)
                final -= curr
                curr += 2
            ans[-1] += final
        return ans
