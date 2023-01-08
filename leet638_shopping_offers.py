class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.memo = {}
        return self.find_lowest_price(price, special, needs)

    def find_lowest_price(self, price, special, needs):
        # memoization
        if tuple(needs) in self.memo:
            return self.memo[tuple(needs)]
        # total cost without offers
        cost = 0
        for idx, need in enumerate(needs):
            cost += need * price[idx]
        # take one offer
        for offer in special:
            for idx, need in enumerate(needs):
                if need < offer[idx]: # can't use the offer
                    break
            else:
                new_needs = [need - offer[i] for i, need in enumerate(needs)]
                cost = min(cost, offer[-1] + self.find_lowest_price(price, special, new_needs))
        self.memo[tuple(needs)] = cost
        return cost
