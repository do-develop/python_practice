class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        i, j = 0, 0
        curr = 0

        while i < len(buses):
            curr = 0
            while j < len(passengers) and curr < capacity and passengers[j] <= buses[i]:
                j += 1
                curr += 1

            if i == len(buses) - 1:
                j -= 1
                if curr < capacity:
                    time = buses[i]
                    while j >= 0 and time == passengers[j]:
                        time -= 1
                        j -= 1
                    return time
                else:
                    time = passengers[j] - 1
                    j -= 1
                    while j >= 0 and time == passengers[j]:
                        time -= 1
                        j -= 1
                    return time
            i += 1

        return buses[-1]
