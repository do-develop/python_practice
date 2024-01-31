class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # Sort times by arrival time, and simulate the seat assignment process.
        available, leave_times = list(range(len(times))), []
        for arrival, leaving in sorted(times):
            while leave_times and leave_times[0][0] <= arrival:
                heappush(available, heappop(leave_times)[1])
            if arrival == times[targetFriend][0]:
                return available[0]
            heappush(leave_times, (leaving, heappop(available)))
