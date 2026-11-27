class Solution:
    def minAllOneMultiple(self, k: int) -> int:
        rem = 1 % k
        count = 1
        found = set()

        while rem not in found:
            if rem == 0:
                return count
            
            found.add(rem)
            rem = (rem * 10 + 1) % k
            count += 1
        
        return -1