class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        N = len(stockPrices)
        lines = N - 1 # possible max lines
        stockPrices.sort()

        for i in range(1, N - 1):
            # compare three adjacent points to check if two slope of lines are connected
            # uses cross multiplications
            p1, p2, p3 = stockPrices[i-1], stockPrices[i], stockPrices[i+1]
            if (p2[0] - p1[0]) * (p3[1] - p2[1]) == (p3[0] - p2[0]) * (p2[1] - p1[1]):
                lines -= 1
        return lines
