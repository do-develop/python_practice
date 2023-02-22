# linear transformation approach
class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        dim = len(img1)

        def non_zero_cells(matrix):
            ret = []
            for x in range(dim):
                for y in range(dim):
                    if matrix[x][y] == 1:
                        ret.append((x, y))
            return ret

        transform_count = defaultdict(int)
        max_overlap = 0

        img1_ones = non_zero_cells(img1)
        img2_ones = non_zero_cells(img2)

        for (x1, y1) in img1_ones:
            for (x2, y2) in img2_ones:
                vec = (x2 - x1, y2 - y1)
                transform_count[vec] += 1
                max_overlap = max(max_overlap, transform_count[vec])
        return max_overlap
