class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # two pointers approach O(N)
        N = len(nums)
        pos_idx, neg_idx = 0, 1
        rearranged = [0] * N

        for i in range(N):
            if nums[i] > 0:
                rearranged[pos_idx] = nums[i]
                pos_idx += 2
            if nums[i] < 0:
                rearranged[neg_idx] = nums[i]
                neg_idx += 2
        return rearranged
