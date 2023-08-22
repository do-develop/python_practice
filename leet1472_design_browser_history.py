class BrowserHistory:

    def __init__(self, homepage: str):
        # two stacks for history and future
        self.history, self.future = [], []
        self.current = homepage

    def visit(self, url: str) -> None:
        # Push 'current' in 'history' stack and mark 'url' as 'current'.
        self.history.append(self.current)
        self.current = url
        self.future = []  # clear the foward history

    def back(self, steps: int) -> str:
        # Pop elements from 'history' stack, and push elements in 'future' stack.
        while steps > 0 and self.history:
            self.future.append(self.current)
            self.current = self.history.pop()
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        # Pop elements from 'future' stack, and push elements in 'history' stack.
        while steps > 0 and self.future:
            self.history.append(self.current)
            self.current = self.future.pop()
            steps -= 1
        return self.current


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
