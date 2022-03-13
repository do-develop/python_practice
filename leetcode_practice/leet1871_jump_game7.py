"""
You are given a 0-indexed binary string s and two integers minJump and maxJump.
In the beginning, you are standing at index 0, which is equal to '0'. You can
move from index i to index j if the following conditions are fulfilled:
i + minJump <= j <= min(i + maxJump, s.length - 1), and s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.
"""

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        reachable = [False] * len(s)
        reachable[0] = True
        start = 0  # farthest start

        for i in range(len(s)):
            if reachable[i] and s[i] == '0':
                l = max(start, i + minJump)
                r = min(i + maxJump, len(s)-1)
                for j in range(l, r+1):
                    reachable[j] = True

                start = r + 1
                if start > len(s):
                    break

        return reachable[-1] and s[len(s)-1] == '0'
        


# TEST
s = "0111111111111111111111111111111101111101111111111111111110"
minJump = 5
maxJump = 26
print(Solution().canReach(s, minJump, maxJump))
# expected output: false
"""
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.

s = "01101110", minJump = 2, maxJump = 3 --> False
"""
