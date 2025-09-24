class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        intensity = defaultdict(list)
        result = []

        def getRegionAverage(r, c):
            if r + 3 > rows or c + 3 > cols:
                return -1
            total = 0
            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    if i + 1 < r + 3 and abs(image[i][j] - image[i+1][j]) > threshold:
                        return -1
                    if j + 1 < c + 3 and abs(image[i][j] - image[i][j+1]) > threshold:
                        return -1
                    total += image[i][j]
            return total//9

        
        for r in range(rows):
            result.append(image[r][:])
            for c in range(cols):
                average = getRegionAverage(r, c)
                if average != -1:
                    for i in range(r, r+3):
                        for j in range(c, c+3):
                            intensity[(i,j)].append(average)

        for r in range(rows):
            for c in range(cols):
                if intensity[(r, c)]:
                    result[r][c] = sum(intensity[(r, c)])//len(intensity[r,c])

        return result