class Solution:
    def placeWordInCrossword(self, board: List[List[str]], word: str) -> bool:
        words = [word, word[::-1]]
        N = len(word)
        for B in board, zip(*board):
            for row in B:
                q = ''.join(row).split('#')
                for w in words:
                    for s in q:
                        if len(s) == N:
                            if all(s[i] == w[i] or s[i] == ' ' for i in range(N)):
                                return True
        return False
