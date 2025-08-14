class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_sorted = sorted(nums)

        curr_grp = 0
        num_to_grp = {}
        num_to_grp[nums_sorted[0]] = curr_grp

        grp_to_list = {}
        grp_to_list[curr_grp]  = deque([nums_sorted[0]])

        for i in range(1, len(nums)):
            if abs(nums_sorted[i] - nums_sorted[i-1]) > limit:
                curr_grp += 1
            
            num_to_grp[nums_sorted[i]] = curr_grp

            if curr_grp not in grp_to_list:
                grp_to_list[curr_grp] = deque()
            grp_to_list[curr_grp].append(nums_sorted[i])

        for i in range(len(nums)):
            num = nums[i]
            grp = num_to_grp[num]
            nums[i] = grp_to_list[grp].popleft()
        return nums
