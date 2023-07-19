class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = [arr[0]]
        for i in range(1, len(arr)):
            prefix_xor.append(prefix_xor[i-1] ^ arr[i])
        
        ans = []
        for l, r in queries:
            if (l == 0):
                ans.append(prefix_xor[r])
            else:
                ans.append(prefix_xor[l - 1] ^ prefix_xor[r])
        return ans
