class Solution:
    def lastRemaining(self, n: int) -> int:
        left = True
        remaining = n
        step = 1
        head = 1
        while remaining > 1:
            # condition that the head will be moved by the step
            # remove from left or odd number amount left
            if left or remaining % 2 == 1:
                head = head + step
            # after removal only half left
            remaining = remaining // 2
            step = step * 2
            left = not left
        return head
