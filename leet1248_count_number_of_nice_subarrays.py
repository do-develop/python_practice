class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_cnt = total_sub = cur_sub = start = 0

        for end in range(len(nums)):
            if nums[end] % 2:
                odd_cnt += 1
                cur_sub = 0
            
            while odd_cnt == k:
                if nums[start] % 2:
                    odd_cnt -= 1
                cur_sub += 1
                start += 1
            
            total_sub += cur_sub
        return total_sub
