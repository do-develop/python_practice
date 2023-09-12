class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n = len(position)

        def count_balls(d):
            count, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    count += 1
                    curr = position[i]
            return count

        left, right = 1, position[n-1] - position[0]
        while left <= right:
            mid = (left + right) // 2
            if count_balls(mid) >= m:
                left = mid + 1
            else:
                right = mid - 1
        return right # return maximum
