class Solution:
    # simple simulation approach
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        curr_cap = capacity

        for i in range(len(plants)):
            if plants[i] <= curr_cap:
                steps += 1
                curr_cap -= plants[i]
            else:
                steps += i * 2 + 1
                curr_cap = capacity - plants[i]
        return steps
