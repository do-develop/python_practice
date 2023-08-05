class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def power(n):
            if n in self.dic:
                return self.dic[n]
            if n % 2:
                self.dic[n] = power(3 * n + 1) + 1
            else:
                self.dic[n] = power(n // 2) + 1
            return self.dic[n]
        
        self.dic = {1: 0} # base case
        pow_num_pair = [n for n in range(lo, hi + 1)]
        pow_num_pair = sorted(pow_num_pair, key=lambda x:(power(x), x))

        return pow_num_pair[k - 1]

        
