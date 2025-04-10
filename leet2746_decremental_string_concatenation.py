class Solution:
    def minimizeConcatenatedLength(self, words: List[str]) -> int:
        N = len(words)

        @cache
        def helper(i, first, last):
            if i >= N:
                return 0

            y = words[i]
            # case x + y
            case1 = helper(i + 1, first, y[-1])
            if last == y[0]:
                case1 += 1

            # case y + x
            case2 = helper(i + 1, y[0], last)
            if y[-1] == first:
                case2 += 1

            return max(case1, case2)

        total = 0
        for w in words:
            total += len(w)
        
        overwrap = helper(1, words[0][0], words[0][-1])
        return total - overwrap
