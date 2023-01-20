class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        sub_sum = total // k
        subset = [0] * k
        nums.sort(reverse=True)

        def partition(idx):
            if idx == len(nums):
                return True
            
            for i in range(k):
                if subset[i] + nums[idx] <= sub_sum:
                    subset[i] += nums[idx]
                    if partition(idx + 1):
                        return True                  
                    subset[i] -= nums[idx]
                    # below means the backtracking failed for that subset
                    # search further would be meaningless
                    if subset[i] == 0:
                        break
            return False
        
        return partition(0)
