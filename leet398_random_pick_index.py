# reservoir sampling
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        sample_cnt = 0      # how many samples with 'target' seen so far
        reservoir = 0       # selected index
        
        for idx, val in enumerate(self.nums):
            if val != target:
                continue
            if sample_cnt == 0: # found first target just save the index
                sample_cnt = 1
                reservoir = idx
            else:               # more than one target, randomly select
                random_pick = randint(0, sample_cnt)
                if random_pick == sample_cnt:
                    reservoir = idx
                sample_cnt += 1
        return reservoir
                
