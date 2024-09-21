class SmallestInfiniteSet:

    def __init__(self):
        self.curr = 1 # current smallest
        self.infiset = set()

    def popSmallest(self) -> int:
        if self.infiset:
            smallest = min(self.infiset)
            self.infiset.remove(smallest)
            return smallest
        else:
            self.curr += 1
            return self.curr - 1

    def addBack(self, num: int) -> None:
        if self.curr > num:
            self.infiset.add(num)
