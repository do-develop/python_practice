class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        lonely = []

        for num, cnt in count.items():
            if cnt == 1 and count[num-1] == count[num+1] == 0:
                lonely.append(num)
        return lonely
