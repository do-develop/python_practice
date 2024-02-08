class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        # i and 2i appear 4 times and every value in between i and 2i appears 8 times
        # total apples = (i * 4 + 2 * i * 4) + ((i + 1)+ (i + 2) ... (i * 2 - 1)) *  8
        side, curr = 2, 12
        if (neededApples <= 12):
            return 8
        while curr < neededApples:
            side += 2
            curr = (side * (side + 1) * (side + 2)) // 2
        return side * 4
