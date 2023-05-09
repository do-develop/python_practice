class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        i, n = 0, len(barcodes)
        res = [0] * n
        count = collections.Counter(barcodes)
        for k, v in count.most_common(): # sort by most common order
            for _ in range(v):
                res[i] = k
                i += 2 # step by 2
                if i >= n: 
                    i = 1 # it is guarenteed an answer exists
        return res
                    
