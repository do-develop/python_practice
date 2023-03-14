class FreqStack:

    def __init__(self):
        self.count = {}
        self.max_count = 0
        self.stacks = {}

    def push(self, val: int) -> None:
        val_cnt = 1 + self.count.get(val, 0)
        self.count[val] = val_cnt
        if val_cnt > self.max_count:
            self.max_count = val_cnt
            self.stacks[val_cnt] = []
        self.stacks[val_cnt].append(val)

    def pop(self) -> int:
        res = self.stacks[self.max_count].pop()
        self.count[res] -= 1
        if not self.stacks[self.max_count]:
            self.max_count -= 1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
