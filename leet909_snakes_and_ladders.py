class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # BFS to find the shortest path
        length = len(board)
        board.reverse() # reverse to rearranged the order of rows
        # convert the square value(position) to coordinates
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2: # odd row
                c = length - 1 - c
            return [r, c]
        
        q = deque() # [position, moves]
        q.append([1, 0])
        visit = set()
        while q:
            pos, moves = q.popleft()

            for i in range(1, 7): # dice 1 to 6
                next_pos = pos + i
                r, c = intToPos(next_pos)
                if board[r][c] != -1: # found snake or ladder
                    next_pos = board[r][c]
                if next_pos == length * length: # reached destination
                    return moves + 1
                if next_pos not in visit:
                    visit.add(next_pos)
                    q.append([next_pos, moves + 1])
        return -1
