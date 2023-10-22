class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ops, count = 0, Counter(nums)
        for val1, cnt in count.items():
            val2 = k - val1
            # to remove duplicate pair, consider only pairs where val1 >= val2
            if val2 < val1 or val2 not in count:
                continue
            ops += min(cnt, count[val2]) if val1 != val2 else cnt // 2
        return ops
