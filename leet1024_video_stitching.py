class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        # sort and then greedy approach
        prev_end, end, cnt = -1, 0, 0
        # s = start , e = end
        for s, e in sorted(clips):
            # stitching not doable or completed?
            if s > end or end >= time: 
                break
            elif prev_end < s <= end:
                prev_end = end
                cnt += 1
            end = max(end, e)
        return cnt if end >= time else -1
