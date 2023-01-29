class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for new in asteroids:
            while stack and new < 0 < stack[-1]:
                if stack[-1] < -new:
                    stack.pop()
                    continue # new is added to the stack
                elif stack[-1] == -new:
                    stack.pop()
                break        # both new and last asteroid collided
            else:
                stack.append(new)
        return stack
