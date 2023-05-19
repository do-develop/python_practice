class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        res = []
        node_count = 1
        height = 1
        # get the height of the label
        while label >= node_count * 2:
            node_count *= 2
            height += 1
        # iterate from the target label to the root
        while label != 0:
            res.append(label)
            level_max = 2 ** (height) - 1
            level_min = 2 ** (height - 1)
            label = int((level_max + level_min - label) / 2) # move to the parent
            height -= 1
        return res[::-1]
