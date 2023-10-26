class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # The optimum strategy for each is to select the rock for which the greatest
        # sum of points is at risk. We sort the indices with that key, and then keep 
        # track of scores as Alice and Bob take their turns.   
        pair = sorted(zip(aliceValues, bobValues), key=lambda x: -sum(x)) # descending order
        a = sum([i[0] for i in pair[0::2]])
        b = sum([i[1] for i in pair[1::2]])

        return (a >= b) - (a <= b)
