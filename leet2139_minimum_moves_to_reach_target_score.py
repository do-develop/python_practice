class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0

        while maxDoubles > 0 and target > 1:
            if target % 2 == 0:
                moves += 1
            else:
                moves += 2
            target = target // 2
            maxDoubles -= 1
        return moves + target - 1
