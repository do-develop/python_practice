class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # buy  - max heap
        # sell - min heap
        buy, sell = [], []
        for price, amt, order in orders:
            if order: heappush(sell, (price, amt))
            else: heappush(buy, (-price, amt))

            while buy and sell and -buy[0][0] >= sell[0][0]:
                (bprice, bamt), (sprice, samt) = heappop(buy), heappop(sell)

                if bamt > samt: heappush(buy, (bprice, bamt - samt))
                elif bamt < samt: heappush(sell, (sprice, samt - bamt))

        return sum(amt for _, amt in buy + sell) % 1000_000_007
