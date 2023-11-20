class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        # linear search approach
        ptr = 0 # pointer
        groups.reverse()

        while ptr <= len(nums):
            if len(groups) == 0:
                return True
            curr_grp = groups[-1]
            if nums[ptr:ptr + len(curr_grp)] == curr_grp:
                ptr += len(curr_grp)
                groups.pop()
            else:
                ptr += 1
        return False
