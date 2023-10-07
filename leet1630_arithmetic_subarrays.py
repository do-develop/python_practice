class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        isArithmetic = False
        res = []
        for i in range(len(l)):
            arr = sorted(nums[l[i]:r[i] + 1])
            if len(arr) == 1 or len(arr) == 2:
                res.append(True)
                continue
            for j in range(1, len(arr) - 1):
                if arr[j-1] - arr[j] == arr[j] - arr[j+1]:
                    isArithmetic = True
                else:
                    isArithmetic = False
                    break
            res.append(isArithmetic)
        return res
