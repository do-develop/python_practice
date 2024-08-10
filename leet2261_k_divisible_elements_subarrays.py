class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        N = len(nums)
        sub_arrays = set()

        for i in range(N):
            count = 0

            for j in range(i, N):
                if nums[j] % p == 0:
                    count += 1

                if count > k:
                    break
                sub_arrays.add(tuple(nums[i:j + 1]))
        
        return len(sub_arrays)
