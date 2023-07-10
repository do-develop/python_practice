class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_dict = defaultdict(list)
        groups = []

        for i, size in enumerate(groupSizes):
            group_dict[size].append(i)
            if(len(group_dict[size]) == size):
                groups.append(group_dict[size])
                del group_dict[size]
        return groups
