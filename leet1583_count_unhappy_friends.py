class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        closer = {}
        # people they are closer to than the person they are paired with
        for x, y in pairs:
            closer[x] = preferences[x][:preferences[x].index(y)]
            closer[y] = preferences[y][:preferences[y].index(x)]
        
        unhappy =  0
        for x in closer:
            for closer_friend in closer[x]:
                if x in closer[closer_friend]:
                    unhappy += 1
                    break
        return unhappy
