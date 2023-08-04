class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        

    def push(self, x: int) -> None:
        if len(self.stack) < self.size :
            self.stack.append([x, 0])

    def pop(self) -> int:
        if not self.stack:
            return -1
        
        res, inc = self.stack.pop()
        res += inc
        if self.stack:
            self.stack[-1][1] += inc
        return res

    def increment(self, k: int, val: int) -> None:
        if self.stack:
            self.stack[min(k, len(self.stack)) - 1][1] += val
