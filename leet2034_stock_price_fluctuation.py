class StockPrice:

    def __init__(self):
        self.timestamps = {}
        self.highestTimestamp = 0
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp: int, price: int) -> None:
	    # to keep track of current prices
        self.timestamps[timestamp] = price
        self.highestTimestamp = max(self.highestTimestamp, timestamp)
        
		# for maximum/minimum
        heappush(self.minHeap, (price, timestamp))
        heappush(self.maxHeap, (-price, timestamp))

    def current(self) -> int:
        return self.timestamps[self.highestTimestamp]

    def maximum(self) -> int:
        currPrice, timestamp = heappop(self.maxHeap)
        while -currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.maxHeap)
            
        heappush(self.maxHeap, (currPrice, timestamp))
        return -currPrice

    def minimum(self) -> int:
        currPrice, timestamp = heappop(self.minHeap)
        while currPrice != self.timestamps[timestamp]:
            currPrice, timestamp = heappop(self.minHeap)
            
        heappush(self.minHeap, (currPrice, timestamp))
        return currPrice


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
