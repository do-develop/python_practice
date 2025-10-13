class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        N = len(grid)
        mid = N // 2

        y = ((grid[i][i], grid[N - i - 1][mid], grid[i][N - i - 1]) for i in range(mid))

        cnt1 = Counter(chain(*y))
        cnt1[grid[mid][mid]] += 1

        cnt2 = Counter(chain(*grid)) - cnt1

        return N * N - max(cnt1[0]+ cnt2[1], cnt1[0]+ cnt2[2], cnt1[1]+ cnt2[0], cnt1[1]+ cnt2[2], cnt1[2]+ cnt2[0], cnt1[2]+ cnt2[1])
