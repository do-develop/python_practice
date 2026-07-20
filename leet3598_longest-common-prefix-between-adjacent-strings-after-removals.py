class Solution:
    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        N = len(words)
        suffix = [0] * N
        prefix = [0] * N

        if N == 1:
            return [0]
        
        def lcp(s, t):
            n = min(len(s), len(t))
            i = 0
            while i < n:
                if s[i] != t[i]:
                    return i
                i += 1
            return i

        for i in range(1, N):
            prefix[i] = max(prefix[i - 1], lcp(words[i], words[i - 1]))
        
        for i in range(N - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], lcp(words[i], words[i + 1]))

        ans = []

        for i in range(N):
            if i < 1:
                ans.append(suffix[i+1])
                continue

            if i == N - 1:
                ans.append(prefix[i-1])
                continue
            
            ans.append(max(prefix[i - 1], suffix[i + 1], lcp(words[i-1], words[i+1])))

        return ans
