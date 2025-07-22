class Solution:
    def minGroupsForValidAssignment(self, balls: List[int]) -> int:
        ball_counter = Counter(balls)
        if len(ball_counter) == 1:
            return 1
        

        def search(num):
            ans = 0
            for key in ball_counter:
                temp = ball_counter[key] % num
                if temp > ball_counter[key] // num:
                    return 0
            
                ans += ceil(ball_counter[key] / (num + 1))
            return ans


        mini, maxi = 1, min(ball_counter.values())
        ans = float('inf')
        for i in range(mini, maxi + 1):
            groups = search(i)
            if groups:
                ans = min(ans, groups)
        return ans