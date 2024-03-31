class Solution:
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        # BFS approach
        seen = set([start])
        search = [(0, start)]

        for ops, num in search:
            if num == goal:
                return ops
            if 0 <= num <= 1000:
                for n in nums:
                    for next_n in (num ^ n, num - n, num + n):
                        if next_n not in seen:
                            seen.add(next_n)
                            search.append((ops + 1, next_n))

        return -1
