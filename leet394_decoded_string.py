class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = "" # keep track of decoded string
        cur_num = 0
        
        for c in s:
            if c == '[':
                stack.append((cur_str, cur_num))
                # reset
                cur_str = ""
                cur_num = 0
            elif c == ']':
                last_str, last_num = stack.pop(-1)
                cur_str = last_str + last_num * cur_str
            elif c.isdigit():
                cur_num = cur_num * 10 + int(c)
            else:
                cur_str += c
        
        return cur_str
