class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) > len(list2):
            return self.findRestaurant(list2, list1)
        # create a dictionary of the smaller list
        dic = {v: i for i, v in enumerate(list1)}

        min_sum = float('inf') # minimum index sum
        found = []
        for i, v in enumerate(list2):
            if v in dic:
                idx_sum = dic[v] + i
                if idx_sum < min_sum:
                    min_sum = idx_sum
                    del found[:]
                    found.append(v)
                elif idx_sum == min_sum:
                    found.append(v)
        return found

