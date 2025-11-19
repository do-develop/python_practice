class Solution:
    def minAnagramLength(self, s: str) -> int:
        stringList = list(s)
        N = len(s)

        for size in range(1, N):
            if N % size == 0:
                initialList = sorted(stringList[:size])
                for j in range(size, N, size):
                    substr = stringList[j:j + size]
                    substr.sort()

                    if initialList != substr:
                        break
                # if the loop never breaks, this size is valid
                else:
                    return size
        # if nothing matches then the entire string is the answer
        return N
