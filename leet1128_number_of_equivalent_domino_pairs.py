class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = collections.defaultdict(int)
        ans = 0
        for x, y in dominoes:
            if x > y:
                x, y = y, x
            value = 10 * x + y
            # if an equal pair is found
            if value in counter:
                # it matches with previously found pairs too
                ans += counter[value]
            counter[value] += 1
        return ans
