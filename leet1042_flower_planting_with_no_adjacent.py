class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # connected gardens in graph
        graph = collections.defaultdict(list)
        for x, y in paths:
            graph[x].append(y)
            graph[y].append(x)
        
        plant = {i: 0 for i in range(1, n + 1)}
        for garden in graph:
            flower = set(range(1, 5)) # four types of flower
            for each in graph[garden]:
                if plant[each] != 0 and plant[each] in flower:
                    flower.remove(plant[each])
            plant[garden] = flower.pop()
        return [plant[x] if plant[x] != 0 else 1 for x in range(1, n + 1)]
        
