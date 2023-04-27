class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:

        def pattern_match(p: str, q: str) -> bool:
            pi = 0 # pattern index
            for _, c in enumerate(q):
                if pi < len(p) and p[pi] == c:
                    pi += 1
                elif c.isupper():
                    return False
            return pi == len(p)
        return [pattern_match(pattern, q) for q in queries]

                
