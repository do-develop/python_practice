class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0], -x[1]))
        stack = []
        ans = 0

        for _, dfc in properties:
            while stack and stack[-1] < dfc:
                stack.pop()
                ans += 1
            stack.append(dfc)
        return ans
