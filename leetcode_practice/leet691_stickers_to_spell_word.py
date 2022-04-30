"""
We are given n different types of stickers. Each sticker has a lowercase
English word on it. You would like to spell out the given string target by
cutting individual letters from your collection of stickers and rearranging
them. You can use each sticker more than once if you want, and you have
infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If
the task is impossible, return -1. Note: In all test cases, all words were
chosen randomly from the 1000 most common US English words, and target was
chosen as a concatenation of two random words.
"""
from typing import List
class Solution:
    def minStickers(self, stickers: List[str], target: str) -> int:
        stick_count = []

        for i, s in enumerate(stickers):
            stick_count.append({})
            for c in s:
                stick_count[i][c] = 1 + stick_count[i].get(c, 0)

        dp = {} # key = subseq of target | val = min num of stickers

        def dfs(t, sticker):
            if t in dp:
                return dp[t]

            result = 1 if sticker else 0
            remainT = ""
            
            for c in t:
                if c in sticker and sticker[c]> 0:
                    sticker[c] -= 1
                else:
                    remainT += c

            if remainT:
                used = float("inf")

                for s in stick_count:
                    if remainT[0] not in s:
                        continue
                    used = min(used, dfs(remainT, s.copy()))
                dp[remainT] = used
                result += used
                
            return result
                    



        result = dfs(target, {})
        return result if result != float("inf") else -1



# TEST
stickers = ["with","example","science"]
target = "thehat"
print(Solution().minStickers(stickers, target))
# expected output: 3
