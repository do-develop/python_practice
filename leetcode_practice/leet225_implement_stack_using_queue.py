"""
Implement a last-in-first-out (LIFO) stack using only two queues.
The implemented stack should support all the functions of a normal
stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
"""

from collections import deque

class MyStack:

    def __init__(self):
        self.__main_queue = deque()
        self.__sub_queue = deque()

    def push(self, x: int) -> None:
        self.__main_queue.append(x)

    def pop(self) -> int:
        ret = None
        while len(self.__main_queue) > 1:
            temp = self.__main_queue.popleft()
            self.__sub_queue.append(temp)

        if len(self.__main_queue) == 1:
            ret = self.__main_queue.popleft()
            self.__main_queue, self.__sub_queue = self.__sub_queue, self.__main_queue
        return ret

    def top(self) -> int:
        return self.__main_queue[-1]

    def empty(self) -> bool:
        return False if self.__main_queue else True

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

print(param_2, param_3, param_4, sep=', ')