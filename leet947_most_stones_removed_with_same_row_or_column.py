class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # the questions is asking for the number of islands
        # which they are connected by row or column
        rows, cols = collections.defaultdict(list), collections.defaultdict(list)
        for r, c in stones:
            rows[r].append(c)
            cols[c].append(r)
        
        seen = set()
        def dfs(r, c):
            # connect by same row, r
            for col in rows[r]:
                if (r, col) not in seen:
                    seen.add((r, col))
                    dfs(r, col)
            # connect by same column, c
            for row in cols[c]:
                if(row, c) not in seen:
                    seen.add((row, c))
                    dfs(row, c)
        islands = 0
        for r, c in stones:
            if (r, c) not in seen:
                islands += 1
                dfs(r, c)
        return len(stones) - islands
