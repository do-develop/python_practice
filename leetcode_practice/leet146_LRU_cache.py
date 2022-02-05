"""
Design a data structure that follows the constraints of a Least Recently Used
(LRU) cache.
"""
from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        value = self.cache.get(key, -1)
        if value != -1:
            self.cache.move_to_end(key, last=True)
        return value

    def put(self, key: int, value: int) -> None:
        if self.cache.get(key, False):
            self.cache.move_to_end(key, last=True)
        elif len(self.cache) == self.cap:
            self.cache.popitem(last=False)
        self.cache[key] = value
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4


📃 popitem(last=True)
last=True : The pairs(key-value) are returned in LIFO(Last In First Out)
last=False : The pairs(key-value) are returned in FIFO(First In First Out)

📃 move_to_end(key,last=True)
last=True : The item is moved to the right
last=False : The item is moved to the left
"""

