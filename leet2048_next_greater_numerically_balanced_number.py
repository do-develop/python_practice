class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        # permuation and binary search approach
        # given constraint is 0<=n<=10^6(1000000), 1224444 is the smallest number to contains 7 digits
        beautifulnums = [1, 22, 122, 333, 1333, 4444, 44441, 55555, 22333, 122333, 155555, 224444, 666666, 1224444]
        beautifulnums = [str(num) for num in beautifulnums]
        candidates = []

        for num in beautifulnums:
            perm = set("".join(p) for p in itertools.permutations(list(num)))
            candidates += list(perm)

        candidates = [int(c) for c in candidates]
        candidates.sort()
        idx = bisect.bisect_right(candidates, n)
        return candidates[idx]
