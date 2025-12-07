class Solution:
    def clearStars(self, s: str) -> str:
        count = [[] for _ in range(26)]
        arr = list(s)

        for i, c in enumerate(arr):
            if c != '*':
                count[ord(c) - ord('a')].append(i)
            else :
                for j in range(26):
                    if count[j]:
                        arr[count[j].pop()] = '*'
                        break
        return ''.join(c for c in arr if c != '*')
