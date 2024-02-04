class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)

        scores = [[0] * m for _ in range(m)]
        for i in range(m):
            for j in range(m):
                scores[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))

        ans = 0
        for perm in permutations(range(m)):
            ans = max(ans, sum(scores[i][j] for i, j in zip(perm, range(m))))
        return ans
