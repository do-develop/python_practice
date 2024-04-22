class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        # all possible number ranges 100 - 999
        numbers = []
        digit_counter = Counter(digits)
        for first in range(1, 10):
            for second in range(0, 10):
                for third in range(0, 10, 2):
                    if digit_counter[first] > 0 and digit_counter[second] > (first == second) and digit_counter[third] > (first == third) + (second == third):
                        numbers.append(first * 100 + second * 10 + third)
        return numbers
