class Solution:
    def numWays(self, s: str) -> int:
        ones, n, mod = s.count('1'), len(s), 10**9 + 7
        if ones == 0:
            return (n-2)*(n-1) //2 % mod
        if ones % 3 != 0:
            return 0
        
        ones_in_split = ones // 3
        count = first_cut = second_cut = 0
        
        for c in s:
            if c == '1':
                count += 1
            if count == ones_in_split:
                first_cut += 1
            elif count == ones_in_split * 2:
                second_cut += 1
        
        return first_cut * second_cut % mod
