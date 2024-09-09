class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        prev_bound = 0
        tax = 0

        for bound, rate in brackets:
            curr = min(income, bound) - prev_bound
            if(curr > 0):
                tax += curr * rate / 100
                prev_bound = bound

        return tax
