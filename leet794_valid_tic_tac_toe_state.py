class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        x_count, o_count = 0, 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'X':
                    x_count += 1
                elif board[r][c] == 'O':
                    o_count += 1
        # handle invalid cases
        if o_count > x_count or x_count - o_count > 1:
            return False
        
        if self.check_win_pos(board, 'O'):
            if self.check_win_pos(board, 'X'):
                return False # only one can win
            return o_count == x_count
        
        if self.check_win_pos(board, 'X') and x_count != o_count + 1:
            return False
        
        return True
        

    def check_win_pos(self, board, player):
        # check rows
        for i in range(len(board)):
            if board[i][0] == board[i][1] == board[i][2] == player:
                return True
        
        # check columns
        for i in range(len(board[0])):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True
        
        # check diagonals
        if board[0][0] == board[1][1] == board[2][2] == player or \
            board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False
