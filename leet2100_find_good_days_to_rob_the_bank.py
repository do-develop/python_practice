# sliding window problem
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        N = len(security)

        pre = [0] * (N + 1)
        post = [0] * (N + 1)

        for i in range(1, N):
            if security[i] <= security[i - 1]:
                pre[i] = pre[i - 1] + 1

        for i in range(N-2, -1, -1):
            if security[i] <= security[i + 1]:
                post[i] = post[i + 1] + 1
        
        goodday = []
        for i in range(time, N - time):
            if pre[i] >= time and post[i] >= time:
                goodday += [i]
        return goodday
