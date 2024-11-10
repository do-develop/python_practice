class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        events = []

        for left, right in intervals:
            events.append((left, 1))
            events.append((right + 1, -1))

        events.sort()

        max_grps = 0
        current_grps = 0

        for _, evt_type in events:
            current_grps += evt_type
            max_grps = max(max_grps, current_grps)
        return max_grps
