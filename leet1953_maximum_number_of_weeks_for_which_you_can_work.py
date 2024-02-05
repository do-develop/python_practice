class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # Greedy approch
        # case 1: sum - max > max 
        # at least two projects will remain until just one remains 
        # with one milestone, all milestones will be removed
        # case 2: 
        # if not, 2 * (sum - max) + 1 will be removed

        total = sum(milestones)
        largest = max(milestones)

        if total >= (largest * 2):
            return total
        else:
            return 2 * (total - largest) + 1
