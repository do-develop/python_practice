class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        #backtracking approach
        def backtrack(sub, idx):
            if len(sub) == len(s):
                res.append(sub)
            else:
                if s[idx].isalpha():
                    backtrack(sub + s[idx].swapcase(), idx + 1)
                backtrack(sub + s[idx], idx + 1)
        backtrack("", 0)
        return res
