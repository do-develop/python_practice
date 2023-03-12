class Solution:
    def numSpecialEquivGroups(self, words: List[str]) -> int:
        # dictionary for equivalent groups
        dic = collections.defaultdict(int)
        for w in words:
            # characters at even index 0, 2, 4 ...
            even = ''.join(sorted(w[0::2]))
            # characters at odd index 1, 3, 5 ...
            odd = ''.join(sorted(w[1::2]))
            # if two different strings have the same sorted string,
            # they are the specal-equivalent strings
            dic[(even, odd)] += 1
        return len(dic)
