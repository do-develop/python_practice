"""
Design your implementation of the circular double-ended queue (deque).
"""
# Definition for singly-linked list.
class Node:
    def __init__(self, value, right_node=None, left_node=None):
        self.value = value
        self.left = right_node  # doubly linked list
        self.right = left_node  # doubly linked list

class MyCircularDeque:

    def __init__(self, k: int):
        self.head, self.tail = Node(None), Node(None)
        self.max_size = k
        self.size = 0
        self.head.right, self.tail.left = self.tail, self.head

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            new_node = Node(value)
            head_next = self.head.right
            self.head.right, head_next.left = new_node, new_node
            new_node.left, new_node.right = self.head, head_next
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            new_node = Node(value)
            tail_before = self.tail.left
            self.tail.left, tail_before.right = new_node, new_node
            new_node.left, new_node.right = tail_before, self.tail
            self.size += 1
            return True
        return False


    def deleteFront(self) -> bool:
        if not self.isEmpty():
            head_right = self.head.right.right
            head_right.left, self.head.right = self.head, head_right
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            tail_before = self.tail.left.left
            tail_before.right, self.tail.left = self.tail, tail_before
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        return self.head.right.value if not self.isEmpty() else -1

    def getRear(self) -> int:
        return self.tail.left.value if not self.isEmpty() else -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max_size

# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(5)
param_1 = obj.insertFront(1)
param_1 = obj.insertFront(2)
param_2 = obj.insertLast(3)
param_2 = obj.insertLast(4)
param_3 = obj.deleteFront()
param_4 = obj.deleteLast()
param_5 = obj.getFront()
param_6 = obj.getRear()
param_7 = obj.isEmpty()
param_8 = obj.isFull()

print(param_1, param_2, param_3, param_4, param_5, param_6, param_7, param_8, sep=", ")