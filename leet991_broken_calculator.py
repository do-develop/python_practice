class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # work backwards to greedily divide by 2
        op_count = 0
        while target > startValue:
            op_count += 1
            if target % 2:  # odd
                target += 1
            else:           # even
                target //= 2
        return op_count + startValue - target
