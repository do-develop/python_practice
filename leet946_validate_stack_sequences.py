class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        pos = 0 # tracking popped positon
        for n in pushed:
            stack.append(n)
            while len(stack) > 0 and stack[-1] == popped[pos]:
                stack.pop()
                pos += 1
        return True if len(stack) == 0 else False
