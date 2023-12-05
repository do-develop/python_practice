class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        d = {k:v for k, v in knowledge}
        tokens = s.split("(")
        ans = tokens[0]

        for i in range(1, len(tokens)):
            keyword, string = tokens[i].split(')')
            ans += d.get(keyword, '?') + string
        return ans
