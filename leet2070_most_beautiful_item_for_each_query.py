class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        N = len(items)
        ans, beauty = [], [items[0][1]] * N
        for i in range(1, N):
            beauty[i] = max(beauty[i - 1], items[i][1])
        
        def bin_search(query_price):
            max_beauty, s, e = 0, 0, N - 1 
            while s <= e:
                m = (s + e) // 2
                if items[m][0] <= query_price:
                    max_beauty = beauty[m]
                    s = m + 1
                else:
                    e = m - 1
            return max_beauty
        
        for query_price in queries:
            ans.append(bin_search(query_price))
        return ans
