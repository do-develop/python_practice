class Solution:
    def digitSum(self, s: str, k: int) -> str:
        def handle_substr(substr):
            return str(sum(int(c) for c in substr))
        
        while len(s) > k :
            digit = ''
            for i in range(0, len(s), k):
                digit += handle_substr(s[i: i + k])

            s = digit
        return s
