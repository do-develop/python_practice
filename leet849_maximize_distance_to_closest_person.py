class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res, last, n = 0, -1, len(seats)
        for i in range(n):
            if seats[i]:
                # check the distance in the middle
                res = max(res, i if last < 0 else (i - last) / 2)
                last = i
        # finally check the distance at the end
        return int(max(res, n - last - 1))
