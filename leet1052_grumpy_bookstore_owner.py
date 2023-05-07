class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        satisfied, unsatisfied, trick_satisfied = 0, 0, 0
        for i, customer in enumerate(customers):
            if not grumpy[i]:
                satisfied += customer
            else:
                unsatisfied += customer
            # reduce the window size
            if (i >= minutes and grumpy[i - minutes]==1):
                unsatisfied -= customers[i-minutes]
            trick_satisfied = max(trick_satisfied, unsatisfied)
        
        return satisfied + trick_satisfied
