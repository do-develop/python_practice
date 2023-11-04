class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res = [0] * (2 * n - 1)
        used = set()

        def backtrack(idx):
            # base case: used all numbers
            if (len(used) == n):
                return res
            if (res[idx]): 
                return backtrack(idx + 1)
            # grab largest number first (greedy)
            for x in range(n, 0, -1):
                if x not in used:
                    sec = idx + x
                    if (x == 1):
                        sec = idx
                    if sec < len(res) and res[idx] == 0 and res[sec] == 0:
                        res[idx], res[sec] = x, x
                        used.add(x)
                        diff_case = backtrack(idx + 1)
                        if diff_case: return diff_case
                        used.remove(x)
                        res[idx], res[sec] = 0, 0
        return backtrack(0)
