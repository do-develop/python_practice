class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        # Compute prefix array of nums. Any at index i, you want to find index j such at
        # prefix[i] <= prefix[j] - prefix[i] <= prefix[-1] - prefix[j]
        prefix = [0] # store prefix sum
        for n in nums:
            prefix.append(prefix[-1] + n)
        
        ans = j = k = 0
        for i in range(1, len(nums)):
            j = max(j, i + 1) #"j = max(j, i+1)" which ensures j does not go back to i+1 if it has advanced ahead of i+1.
            while j < len(nums) and 2 * prefix[i] > prefix[j]:
                j += 1
            k = max(k, j)
            # 2 * prefix[right_boundary] <= prefix[-1] + prefix[i]
            while k < len(nums) and prefix[k] - prefix[i] <=  prefix[-1] - prefix[k]:
                k += 1
            ans += k - j
        return ans % 1_000_000_007
