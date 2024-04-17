# greedy approach
class Solution:
    def minimumBuckets(self, hamsters: str) -> int:
        hamsters = list(hamsters)
        buckets = 0

        for i, v in enumerate(hamsters):
            if v == 'H' and (i == 0 or hamsters[i-1] != '#'):
                if i + 1 < len(hamsters) and hamsters[i + 1] == '.':
                    hamsters[i + 1] = '#'
                elif i and hamsters[i - 1] == '.':
                    hamsters[i - 1] = '#'
                else:
                    return -1
                buckets += 1
        return buckets
