class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        # greedy approach
        # keep selecting the minimum value until there is only one node
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += arr.pop(i) * min(arr[i-(i>0) : i+1])
        return res
