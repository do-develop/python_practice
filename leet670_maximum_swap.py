class Solution:
    def maximumSwap(self, num: int) -> int:
        # make a list to make it iterable
        num = [int(x) for x in str(num)]
        max_idx = len(num) - 1
        # mark the index to swap
        small = big = 0
        for i in range(len(num)-1, -1, -1):
            if num[i] > num[max_idx]:
                max_idx = i
            elif num[i] < num[max_idx]:
                small = i
                big = max_idx
        num[small], num[big] = num[big], num[small]
        return int(''.join([str(x) for x in num]))
