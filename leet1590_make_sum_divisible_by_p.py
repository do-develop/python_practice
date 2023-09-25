class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Calculate the remainder = sum(A) % p 
        # Need to remove a subarray which has remainder to make the rest sum divisible by p
        # Record the prefix sum in a hashmap. last[remainder] = idx records the last index
        # Find the shortest array with sum % p = rem.
        rem = sum(nums) % p
        last = {0: -1}
        cur_rem = 0
        res = n = len(nums)
        for i, v in enumerate(nums):
            cur_rem = (cur_rem + v) % p
            last[cur_rem] = i
            if (cur_rem - rem) % p in last:
                res = min(res, i - last[(cur_rem - rem) % p])
        return res if res < n else -1
