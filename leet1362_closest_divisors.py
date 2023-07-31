class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for n in range(int((num + 2) ** 0.5), 0, -1):
            if((num + 1) % n == 0):
                return [n, (num + 1)//n]
            if((num + 2) % n == 0):
                return [n, (num + 2)//n]
        return []
