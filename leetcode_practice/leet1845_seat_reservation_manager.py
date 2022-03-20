"""
Design a system that manages the reservation state of n seats that are numbered
from 1 to n. Implement the SeatManager class:

SeatManager(int n) Initializes a SeatManager object that will manage n seats
numbered from 1 to n. All seats are initially available. int reserve() Fetches
the smallest-numbered unreserved seat, reserves it, and returns its number.
void unreserve(int seatNumber) Unreserves the seat with the given seatNumber.
"""
import heapq

class SeatManager:

    def __init__(self, n: int):
        self.unreserved = [i for i in range(1, n+1)]
        

    def reserve(self) -> int:
        return heapq.heappop(self.unreserved)
        

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.unreserved, seatNumber)


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)


# TEST
seat_manager = SeatManager(10)
print(seat_manager.reserve())
seat_manager.unreserve(1)

