class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)

param_1 = obj.peek()
param_2 = obj.pop()
param_3 = obj.pop()
param_4 = obj.pop()
param_5 = obj.empty()

print(param_1, param_2, param_3, param_4, param_5, sep=', ')