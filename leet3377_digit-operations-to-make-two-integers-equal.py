class Solution:
    def minOperations(self, n: int, m: int) -> int:
        def is_prime(x):
            if x < 2:
                return False
            if x == 2:
                return True
            if x % 2 == 0:
                return False
            for i in range(3, math.isqrt(x) + 1, 2):
                if x % i == 0:
                    return False
            return True
        
        if is_prime(n) or is_prime(m):
            return -1
        
        def get_neighbors(num):
            digits = list(str(num))
            neighbors = []
            for i, d in enumerate(digits):
                d = int(d)
                if d < 9:
                    digits[i] = str(d + 1)
                    neighbor = int(''.join(digits))
                    neighbors.append(neighbor)
                    digits[i] = str(d)
                if d > 0 and not (i == 0 and d == 1):
                    digits[i] = str(d - 1)
                    neighbor = int(''.join(digits))
                    neighbors.append(neighbor)
                    digits[i] = str(d)
            return neighbors

        dist = {n: n} 
        heap = [(n, n)]
        while heap:
            cost, curr = heapq.heappop(heap)

            if curr == m:
                return cost
            
            if cost > dist.get(curr, float('inf')):
                continue
            
            for neigh in get_neighbors(curr):
                if is_prime(neigh):
                    continue
                new_cost = cost + neigh
                if new_cost < dist.get(neigh, float('inf')):
                    dist[neigh] = new_cost
                    heapq.heappush(heap, (new_cost, neigh))
        
        return -1
