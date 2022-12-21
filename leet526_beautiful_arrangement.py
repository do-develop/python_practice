class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        nums = {i for i in range(1, n + 1)}

        def backtrack(pos, nums):
            if pos == 1: # last item
                self.count += 1
                return
            for i in nums:
                if pos % i == 0 or i % pos == 0:
                    backtrack(pos - 1, nums - {i})
        
        backtrack(n, nums)
        return self.count
