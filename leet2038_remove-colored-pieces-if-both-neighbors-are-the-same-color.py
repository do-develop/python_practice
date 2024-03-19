class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # find substring AAA and BBB
        N = len(colors)
        count_a, count_b = 0, 0

        for i in range(1, N-1):
            if colors[i - 1] == 'A' and colors[i] == 'A' and colors[i + 1] == 'A':
                count_a += 1
            if colors[i - 1] == 'B' and colors[i] == 'B' and colors[i + 1] == 'B':
                count_b += 1
        return count_a > count_b
