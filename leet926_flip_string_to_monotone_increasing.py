class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones = [0] * len(s)
        count = 0 # count of 1 on the LHS
        for i in range(len(s)):
            if s[i] == '1':
                count += 1
            ones[i] = count
        
        prev = 0
        for i in range(1, len(s) + 1):
            if s[i-1] == '0':
                # change right 0s so far vs change left 1s
                curr = min(prev + 1, ones[i - 1])
            else:
                curr = min(prev, ones[i - 1])
            prev = curr
        return prev
