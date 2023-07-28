class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        # min-heap that stores endDay for started events
        started = []
        count = i = 0
        # first day an event started
        curr_day = events[0][0]

        while i < len(events):
            # add all events started on current day
            while i < len(events) and events[i][0] == curr_day:
                heappush(started, events[i][1])
                i += 1
            
            # attend started event that ends the earliest
            heappop(started)
            count += 1
            curr_day += 1

            # remove expired events
            while started and started[0] < curr_day:
                heappop(started)
            # if the 'started' is empty, move to the next day
            if i < len(events) and not started:
                curr_day = events[i][0]

        while started:
            if heappop(started) >= curr_day:
                curr_day += 1
                count += 1
        
        return count
