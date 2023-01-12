class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        seq = defaultdict(int)
        remained = Counter(nums)
        for num in nums:
            # num is already in sequence
            if (not remained[num]):
                continue
            # there is a sequence before this number
            if seq[num - 1] > 0:
                seq[num - 1] -= 1
                seq[num] += 1
                remained[num] -= 1
            # create new sequence
            else:
                if (not remained[num+1] or not remained[num+2]):
                    return False
                remained[num] -= 1
                remained[num+1] -= 1
                remained[num+2] -= 1
                seq[num+2] += 1 # mark the last number of the sequence
        return True
