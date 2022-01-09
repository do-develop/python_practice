import heapq

bundle_count = int(input())

# insert all card bundles in heap
heap = []
for i in range(bundle_count):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    # get first two small card bundles
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
