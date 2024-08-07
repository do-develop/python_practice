class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        position = {}
        N = len(cards)
        pickup = N
        unique = set(cards)
        if len(unique) == N:
            return -1

        for i in range(N):
            if cards[i] in position:
                pickup = min(pickup, i - position[cards[i]] + 1)
                position[cards[i]] = i # update last seen position
            else:
                position[cards[i]] = i 
        return pickup
