"""
Design your implementation of the circular queue. The circular queue
is a linear data structure in which the operations are performed based
on FIFO (First In First Out) principle and the last position is connected
back to the first position to make a circle. It is also called "Ring Buffer".
"""


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.head = 0
        self.tail = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.tail] is None:
            self.q[self.tail] = value
            self.tail = (self.tail + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.head] is None:
            return False
        else:
            self.q[self.head] = None
            self.head = (self.head + 1) % self.maxlen
            return True

    def Front(self) -> int:
        return -1 if self.q[self.head] is None else self.q[self.head]

    def Rear(self) -> int:
        return -1 if self.q[self.tail-1] is None else self.q[self.tail-1]

    def isEmpty(self) -> bool:
        return self.head == self.tail and self.q[self.head] is None

    def isFull(self) -> bool:
        return self.head == self.tail and self.q[self.head] is not None

# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)
param_1 = obj.enQueue(1)
param_1 = obj.enQueue(2)
param_1 = obj.enQueue(3)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()

print(param_1, param_2, param_3, param_4, param_5, param_6, sep=", ")