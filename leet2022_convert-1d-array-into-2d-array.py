class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        arr = []
        k = 0
        for i in range(m):
            arr.append([])
            for j in range(n):
                arr[i].append(original[k])
                k += 1
        return arr
