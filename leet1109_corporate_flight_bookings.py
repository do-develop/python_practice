class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        result = [0] * (n + 1)
        # mark head and tail
        for beg, end, seat in bookings:
            result[beg - 1] += seat
            result[end] -= seat

        # cumulative sume processing
        tmp = 0
        for i in range(n):
            tmp += result[i]
            result[i] = tmp
        return result[:n]
