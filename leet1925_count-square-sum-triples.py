class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        x = [x for x in range(1, n + 1)]
        for i in range(1, n):
            for j in range(1, n):
                a = x[i]
                b = x[j]
                c = (a * a) + (b * b)
                k = math.sqrt(c)
                if k in x:
                    count += 1
        return count
