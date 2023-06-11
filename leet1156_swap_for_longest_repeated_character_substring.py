class Solution:
    def maxRepOpt1(self, text: str) -> int:
        # group by each character
        # [group's key, length]
        group = [[char, len(list(grp))] for char, grp in itertools.groupby(text)]
        counter = collections.Counter(text)
        # extend by 1, check min to filter the case wehre there is no extra char to extend to
        res = max(min(cnt + 1, counter[c]) for c, cnt in group)
        for i in range(1, len(group) - 1):
            if group[i - 1][0] == group[i + 1][0] and group[i][1] == 1:
                res = max(res, min(group[i - 1][1] + group[i + 1][1] + 1, counter[group[i + 1][0]]))
        return res
