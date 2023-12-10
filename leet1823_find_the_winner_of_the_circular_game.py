class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque([x + 1 for x in range(n)])

        while len(q) > 1:
            count = k - 1
            while count:
                q.append(q.popleft())
                count -= 1
            q.popleft()
        return q[0]
