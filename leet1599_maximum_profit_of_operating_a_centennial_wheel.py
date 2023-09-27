class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = -1
        ops = i = cur_round = cur_cust = rem_cust = 0
        while i < len(customers) or rem_cust:
            if i < len(customers):
                rem_cust += customers[i]
                i += 1
            cur_round += 1
            if rem_cust >= 4:
                rem_cust -= 4
                cur_cust += 4
            else:
                cur_cust += rem_cust
                rem_cust = 0
            cur_profit = (cur_cust * boardingCost) - (cur_round * runningCost)
            if (cur_profit > max_profit):
                max_profit = cur_profit
                ops = cur_round
        return -1 if max_profit <= 0 else ops
