class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        moves = 0
        N = len(seats)

        for i in range(N):
            moves += abs(seats[i] - students[i])
        return moves
