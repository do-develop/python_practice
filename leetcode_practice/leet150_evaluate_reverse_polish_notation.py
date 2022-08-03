"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another
expression. Note that division between two integers should truncate toward zero.
It is guaranteed that the given RPN expression is always valid. That means the
expression would always evaluate to a result, and there will not be any division
by zero operation.
"""
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                first, second = stack.pop(), stack.pop()
                stack.append(second - first)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                first, second = stack.pop(), stack.pop()
                stack.append(int(second / first))
            else:
                stack.append(int(c))
        return stack[0]

# TEST
tokens = ["2","1","+","3","*"]
print(Solution().evalRPN(tokens))
#Output: 9
#Explanation: ((2 + 1) * 3) = 9
