class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        res = []
        queens = {(i, j) for i, j in queens} # change to dictionary to faster comparison
        for x in [-1, 0, 1]:
            for y in [-1, 0, 1]: # nine different directions
                for i in range(1, 8):
                    nx, ny = king[0] + x * i, king[1] + y * i
                    if (nx, ny) in queens:
                        res.append([nx, ny])
                        break # no need to find in the same direction
        return res
