class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        grid = [list(row) for row in classroom]
 
        # label each litter cell with its bit index, find start
        litter_count = 0
        start = None
        for r, c in product(range(m), range(n)):
            if grid[r][c] == 'L':
                grid[r][c] = str(litter_count)
                litter_count += 1
            elif grid[r][c] == 'S':
                start = (r, c)
 
        if litter_count == 0:
            return 0
 
        sr, sc = start
        # visited stores the max fuel seen for each (r, c, mask)
        # only revisit a state if more fuel
        visited = defaultdict(int)
        visited[(sr, sc, 0)] = energy
        queue = deque([(sr, sc, energy, 0, 0)])  # r, c, fuel, mask, moves
        full_mask = (1 << litter_count) - 1
 
        while queue:
            r, c, fuel, mask, moves = queue.popleft()
 
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not (0 <= nr < m and 0 <= nc < n) or grid[nr][nc] == 'X':
                    continue
                if fuel == 0:  # can't move
                    continue
 
                cell = grid[nr][nc]
                new_fuel = energy if cell == 'R' else fuel - 1
                new_mask = mask | (1 << int(cell)) if cell.isnumeric() else mask
 
                if new_mask == full_mask:
                    return moves + 1
 
                state = (nr, nc, new_mask)
                if visited[state] < new_fuel:
                    visited[state] = new_fuel
                    queue.append((nr, nc, new_fuel, new_mask, moves + 1))
 
        return -1
