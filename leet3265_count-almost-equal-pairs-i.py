class Solution:
    def countPairs(self, nums: List[int]) -> int:
        pairs = 0
        d = defaultdict(list)

        mxDigit = int(log10(max(nums))) + 1
        # left-pad the string with '0' characters so that each element has max characters.
        nums = map(lambda x: (str(x).rjust(mxDigit, '0')), nums)

        for num in nums:
            d[''.join(sorted(num))].append(num)

        for key in d:
            for str1, str2 in combinations(d[key], 2):
                if sum(c1 != c2 for c1, c2 in zip(str1, str2)) < 3:
                    pairs += 1

        return pairs
