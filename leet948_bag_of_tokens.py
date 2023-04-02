class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # Greedy algorithm
        # sort the token 
        # buy at the cheapest
        # sell at the most expensive
        score = cur_score = 0
        tkn = collections.deque(sorted(tokens))
        while tkn and (tkn[0] <= power or cur_score): # condition that you can play game
            if tkn[0] <= power:
                power -= tkn.popleft() # sell the lowest power
                cur_score += 1
            else:
                power += tkn.pop() # get the highest power
                cur_score -= 1
            score = max(score, cur_score)
        return score
