class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        board = {c: [i//5, i%5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        path = []
        for c in target:
            x, y = board[c]
            # because of 'z' which is in left bottom corner
            # U should come before D
            if y < y0:
                path.append('L' * (y0 - y))
            if x < x0:
                path.append('U' * (x0 - x))
            if y > y0:
                path.append('R' * (y - y0))
            if x > x0:
                path.append('D' * (x - x0))
            path.append('!')
            x0, y0 = x, y
        return "".join(path)
