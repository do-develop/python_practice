class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        frequency = [[freq, c] for c, freq in count.items()]
        frequency.sort(key=lambda x:-x[0]) # sort in decrementing order
        ans = []
        for freq, c in frequency:
            ans.append(freq*c)
        return ''.join(ans)
