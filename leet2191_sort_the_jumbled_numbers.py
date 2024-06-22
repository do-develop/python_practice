class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        # store pair [original, jumbled]
        pairs = []

        for original in nums:
            jumbled = list(str(original))
            for i in range(len(jumbled)):
                jumbled[i] = str(mapping[int(jumbled[i])])
            pairs.append([original, int(''.join(jumbled))])

        pairs.sort(key=lambda x: x[1]) # sort by junmbled number
        for i in range(len(pairs)):
            nums[i] = pairs[i][0] # replace with original number in nums
        
        return nums
