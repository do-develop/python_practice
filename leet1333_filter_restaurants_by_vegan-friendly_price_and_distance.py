class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        candidates = []
        for r in restaurants:
            if (r[2] == veganFriendly or not veganFriendly) and r[3] <= maxPrice and r[4] <= maxDistance:
                candidates.append((r[1], r[0]))
        
        candidates.sort(reverse = True)
        ids = []
        for rate, i in candidates:
            ids.append(i)
        return ids
