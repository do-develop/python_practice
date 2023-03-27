class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        counter = Counter(arr[:1])
        length = len(arr)
        res = 0

        for j in range(1, length - 1):
            for k in range(j + 1, length):
                res = (res + counter[target - arr[k] - arr[j]]) % 1000000007
            counter[arr[j]] += 1
        return res
