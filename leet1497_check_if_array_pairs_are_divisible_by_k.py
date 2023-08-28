class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainders = {i:0 for i in range(k)}
        for a in arr:
            remainders[a%k] += 1
        
        for i in range(k):
            if i == 0:
                if remainders[i] % 2 != 0:
                    return False
            elif remainders[i] != remainders[k - i]:
                return False
        return True
