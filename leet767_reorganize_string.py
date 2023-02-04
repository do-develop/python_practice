class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        chars = [(-counter[c], c) for c in counter]

        heapq.heapify(chars)
        reorganized = []
        prev = None
        while len(chars) > 0:
            _, c = heapq.heappop(chars)
            reorganized.append(c)
            counter[c] -= 1
            # alternate between first and second most frequent letter
            if prev and counter[prev] > 0:
                heapq.heappush(chars, (-counter[prev], prev))
            # store the current as prev before next loop
            prev = c

        return "".join(reorganized) if counter[prev] == 0 else ""
