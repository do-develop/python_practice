# the final position of the elements in the array should be their sorted positions
# Since the array consists of elements from [0, N-1], for any value in the array,
# the corresponding index is where that element must end up in the end.
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        chunks = 0
        chunk_end_idx = arr[0] # minimum index for chunk end

        for i in range(len(arr)):
            chunk_end_idx = max(chunk_end_idx, arr[i])
            if i == chunk_end_idx:
                chunks += 1
        return chunks
