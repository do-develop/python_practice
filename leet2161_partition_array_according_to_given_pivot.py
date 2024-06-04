class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right = [], []

        for n in nums:
            if n < pivot:
                left.append(n)
            elif n == pivot:
                right.insert(0, n)
            else:
                right.append(n)

        left.extend(right)
        return left
