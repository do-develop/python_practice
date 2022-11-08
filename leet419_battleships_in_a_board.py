class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        ROWS, COLS = len(board), len(board[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] != 'X': continue
                if r > 0 and board[r - 1][c] == 'X': continue
                if c > 0 and board[r][c - 1] == 'X': continue
                count += 1
        return count
