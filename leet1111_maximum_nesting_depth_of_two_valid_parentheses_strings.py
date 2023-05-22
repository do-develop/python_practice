class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        groups = []
        depth = 0
        for c in seq:
            if c == '(':
                depth += 1
                groups.append(depth % 2)
            else:
                groups.append(depth % 2)
                depth -= 1
        return groups
