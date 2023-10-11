class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        deletions = 0
        seen = set()

        sorted_freq = sorted(counter.values(), reverse=True)
        for freq in sorted_freq:
            if freq not in seen:
                seen.add(freq)
                continue
            while freq > 0 and freq in seen:
                freq -= 1
                deletions += 1
            seen.add(freq)
        return deletions
