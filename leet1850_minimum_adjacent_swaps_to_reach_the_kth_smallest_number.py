class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        num = list(num)
        original = num.copy()

        for _ in range(k):
            # step 1- in reverse order find first element less than its next
            for i in reversed(range(len(num) - 1)):
                if num[i] < num[i + 1]:
                    idx = i + 1
                    while idx < len(num) and num[i] < num[idx]:
                        idx += 1
                    num[i], num[idx - 1] = num[idx - 1], num[i]
                    lo, hi = i + 1, len(num) - 1
                    while lo < hi:
                        num[lo], num[hi] = num[hi], num[lo]
                        lo += 1
                        hi -= 1
                    break

        count = 0
        for i in range(len(num)):
            idx = i
            while original[i] != num[i]:
                count += 1
                idx += 1
                num[i], num[idx] = num[idx], num[i]
        return count
