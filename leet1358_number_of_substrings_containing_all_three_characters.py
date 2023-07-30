class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left, result, counter = 0, 0, collections.Counter()
        for right, c in enumerate(s):
            counter[c] += 1
            while len(counter) == 3:
                result += len(s) - right    # right side of the window will be valid
                counter[s[left]] -= 1       
                if not counter[s[left]]:
                    del counter[s[left]]
                left += 1                   # decrease the left window
        return result
