class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        end_points = {}
        for line in wall:
            end_len = 0
            for i in range(len(line) - 1): # can ignore right-most end point
                end_len += line[i]
                if end_len in end_points:
                    end_points[end_len] += 1
                else:
                    end_points[end_len] = 1
        counts = end_points.values()
        # length of lines of the wall - max num of the brick end points
        # so that it avoids cutting through bricks as much as possible
        return len(wall) - (max(counts) if counts else 0)
