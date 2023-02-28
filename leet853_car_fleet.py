class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p, s] for p,s in zip(position, speed)]
        stack = []  # to count the car fleet

        for p, s in sorted(pairs)[::-1]:
            stack.append((target - p) / s)  # time required to reach destination
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # it won't be a car fleet
        return len(stack)

            
