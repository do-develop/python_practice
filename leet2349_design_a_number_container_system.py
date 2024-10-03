from sortedcontainers import SortedSet
class NumberContainers:

    def __init__(self):
        self.num_to_idx = defaultdict(SortedSet)
        self.idx_to_num = {}

    def change(self, index: int, number: int) -> None:
        if index in self.idx_to_num:
            old_num = self.idx_to_num[index]
            self.num_to_idx[old_num].discard(index)
            self.idx_to_num[index] = number
            self.num_to_idx[number].add(index)
        else:
            self.idx_to_num[index] = number
            self.num_to_idx[number].add(index)

    def find(self, number: int) -> int:
        found_idxes = self.num_to_idx[number]
        if found_idxes and len(found_idxes) > 0:
            return found_idxes[0]
        else:
            return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
