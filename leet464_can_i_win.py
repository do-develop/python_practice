class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        seen = {}
        summed_choices = (maxChoosableInteger + 1) * maxChoosableInteger / 2
        # if all the choices added up are less than the total, no one can win
        if summed_choices < desiredTotal:
            return False
        # if sum matches the total exactly, then you win if there is odd number of turns
        if summed_choices == desiredTotal:
            return maxChoosableInteger % 2
        
        def helper(chhttps://leetcode.com/contest/oices, remainder):
            if choices[-1] >= remainder:
                return True
            
            # is the result cached before
            seen_key = tuple(choices)
            if seen_key in seen:
                return seen[seen_key]
            
            # for any of the choices I make...
            for i in range(len(choices)):
                # check if the opponent can win
                if not helper(choices[:i] + choices[i+1:], remainder - choices[i]):
                    seen[seen_key] = True
                    return True
            
            seen[seen_key] = False
            return False
        
        # check all permutation
        return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)
