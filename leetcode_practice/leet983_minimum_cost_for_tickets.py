"""
You have planned some train traveling one year in advance. The days of the year
in which you will travel are given as an integer array days. Each day is an
integer from 1 to 365.

Train tickets are sold in three different ways:

a 1-day pass is sold for costs[0] dollars,
a 7-day pass is sold for costs[1] dollars, and
a 30-day pass is sold for costs[2] dollars.
The passes allow that many days of consecutive travel.

For example, if we get a 7-day pass on day 2, then we can travel for 7 days: 2,
3, 4, 5, 6, 7, and 8. Return the minimum number of dollars you need to travel
every day in the given list of days.

 
"""
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}

        for i in range(len(days)-1, -1, -1):
            dp[i] = float("inf")
            for d, c in zip([1,7,30], costs):
                j = i
                while j < len(days) and days[j] < days[i] + d:
                    j += 1
                dp[i] = min(dp[i], c + dp.get(j, 0))
        return dp[0]

        


# TEST
if __name__ == "__main__":
    days = [1,2,3,4,5,6,7,8,9,10,30,31]
    costs = [2,7,15]
    print(Solution().mincostTickets(days, costs))
    
"""
days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
Output: 17
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 30-day pass for costs[2] = $15 which covered days 1, 2, ..., 30.
On day 31, you bought a 1-day pass for costs[0] = $2 which covered day 31.
In total, you spent $17 and covered all the days of your travel.
"""
