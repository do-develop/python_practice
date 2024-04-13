class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.positions = defaultdict(list)
        for i in range(len(arr)):
            self.positions[arr[i]].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        found_positions = self.positions[value]
        found_left = bisect.bisect_left(found_positions, left)
        found_right = bisect.bisect_right(found_positions, right)
        return found_right - found_left



# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
