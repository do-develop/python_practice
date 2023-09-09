class Solution:
    def minInsertions(self, s: str) -> int:
        open_missing = 0    # increment by 1 for every open bracket missing
        close_missing = 0   # increment by 1 for every close bracket missing
        close_needed = 0    # increment by 2 for every open bracket

        for c in s:
            if c == '(':
                if close_needed % 2:
                    close_missing += 1
                    close_needed -= 1
                close_needed += 2
            else:
                close_needed -= 1
                if close_needed < 0:
                    open_missing += 1
                    close_needed += 2
        
        return open_missing + close_missing + close_needed
