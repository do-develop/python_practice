"""
Given a string s, return the lexicographically smallest subsequence
of s that contains all the distinct characters of s exactly once.

# Method 1 - Recursive approach
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for char in sorted(set(s)):
            suffix = s[s.index(char):]  # 문자열에서 해당 값이 존재하는 부분부터 문자열을 슬라이싱한다.
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''
"""
import collections
# Method 2 - Use Stack
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # collections.Counter() --> 문자별 개수를 자동으로 카운팅해 dict형태로 저장한다.
        counter, seen, stack = collections.Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)
        return ''.join(stack)


solution = Solution()
print(solution.removeDuplicateLetters("cbacdcbc"))