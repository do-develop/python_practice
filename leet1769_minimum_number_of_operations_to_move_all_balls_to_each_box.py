class Solution:
    def minOperations(self, boxes: str) -> List[int]: 
        # cost to move all boxes to it is sum of 
        # leftCost to move all left boxes to it, and 
        # rightCost to move all right boxes to it.
        ans = [0] * len(boxes)
        l_cnt, l_cost, r_cnt, r_cost = 0, 0, 0, 0
        N = len(boxes)
        for i in range(1, N):
            if boxes[i - 1] == '1':
                l_cnt += 1
            l_cost += l_cnt
            ans[i] = l_cost
        for i in range(N-2, -1, -1):
            if boxes[i + 1] == '1':
                r_cnt += 1
            r_cost += r_cnt
            ans[i] += r_cost
        return ans
