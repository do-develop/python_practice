class Solution:
    def lengthLongestPath(self, input: str) -> int:
        maxlen = 0
        pathlen = {-1: 0}
        for line in input.split('\n'):
            depth = line.count('\t')
            pathlen[depth] = pathlen[depth - 1] + len(line) - depth
            if line.count('.'):
                maxlen = max(maxlen, pathlen[depth] + depth)
        return maxlen
