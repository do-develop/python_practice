class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        N = len(time)
        # how to count the total number of trips 
        # completed by all buses within that time
        def trip_counter(given_time):
            trips = 0
            for i in range(N):
                trips += given_time // time[i]
                if trips > totalTrips:
                    break
            return trips

        start, end = 0, totalTrips * min(time)
        # binary search to find the minimum time
        while start <= end:
            mid = (start + end) // 2
            trips = trip_counter(mid)

            if trips >= totalTrips:
                end = mid - 1
            else:
                start = mid + 1
        return start
