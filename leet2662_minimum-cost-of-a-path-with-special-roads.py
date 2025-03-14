class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        minHeap = [(0, start[0], start[1])]
        special = defaultdict(list)

        for x1,y1, x2, y2, cost in specialRoads:
            if abs(x2-x1) + abs(y2-y1) < cost:
                continue
            special[(x1, y1)].append((cost, x2, y2))

        visited = {}
        while minHeap:
            currCost, x, y = heappop(minHeap)
            if x == target[0] and y == target[1]:
                return currCost
            if (x, y) in visited:
                continue
            visited[(x, y)] = currCost
            # case 1: if at a starting pos of special road, use it
            if (x, y) in special:
                for specialCost, sx, sy in special[(x, y)]:
                    if (sx, sy) not in visited:
                        heappush(minHeap, (currCost + specialCost, sx, sy))
            
            # case 2: go to a starting pos of a special road
            for sr, sc in special:
                if (sr, sc) not in visited:
                    heappush(minHeap, (currCost + abs(sr-x) + abs(sc-y), sr, sc))
            # case 3: go directly to the target
            heappush(minHeap, (currCost + abs(target[0] - x) + abs(target[1] - y), target[0], target[1]))
