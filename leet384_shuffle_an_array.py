"""
Fisher-Yates algorithm
"""
class Solution:

    def __init__(self, nums: List[int]):
        self.array = nums[:]
        self.original = nums[:]

    def reset(self) -> List[int]:
        self.array = self.original[:]
        return self.array        

    def shuffle(self) -> List[int]:
        arr_len = len(self.array)
        for i in range(arr_len):
            j = randint(i, arr_len - 1)
            self.array[i], self.array[j] = self.array[j], self.array[i]
        return self.array
