class Solution:
    def minimizeStringValue(self, s: str) -> str:
        freq = [0] * 26
        pq = []

        for c in s:
            if c != '?':
                freq[ord(c) - ord('a')] += 1
        
        for i in range(26):
            heapq.heappush(pq, (freq[i], chr(ord('a') + i)))

        temp = ""
        for c in s:
            if c == '?':
                item = heapq.heappop(pq)
                toInsert = item[1]
                frequency = item[0]
                temp += toInsert
                heapq.heappush(pq, (frequency + 1, toInsert))

        temp = ''.join(sorted(temp))
        j = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] == '?':
                s[i] = temp[j]
                j += 1
        
        return ''.join(s)
