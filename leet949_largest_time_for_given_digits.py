class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort(reverse=True) # sort in decreasing order to find the answer earlier
        digit_perm = itertools.permutations(arr) # get all possible permutations

        for digit in digit_perm:
            d1, d2, d3, d4 = digit
            hour = (d1 * 10) + d2
            minute = (d3 * 10) + d4
            if hour < 24 and minute < 60:
                return f"{d1}{d2}:{d3}{d4}"
        return ''
