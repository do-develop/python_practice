class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n + 1) # dp[i]: height for books 0 to i
        dp[0] = 0 # no book, no height

        for i in range(1, n + 1):
            # new row
            cur_w, cur_h = shelfWidth, 0
            j = i - 1
            while j >= 0 and cur_w - books[j][0] >= 0:
                cur_w -= books[j][0]
                cur_h = max(cur_h, books[j][1])     # height of the tallest book in current row
                dp[i] = min(dp[i], dp[j] + cur_h)
                j -= 1
        return dp[n]
