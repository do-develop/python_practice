class Solution:
    def minTime(self, s: str, order: List[int], k: int) -> int:
        # sentinels mark string boundaries
        activated_positions = SortedList([-1, len(s)]) 

        for time, idx in enumerate(order):
            insert_idx = activated_positions.bisect(idx)
            left_neighbor = activated_positions[insert_idx - 1]
            right_neighbor = activated_positions[insert_idx]
            k -= (idx - left_neighbor) * (right_neighbor - idx)
            activated_positions.add(idx)

            if k <= 0 :
                return time

        return -1
