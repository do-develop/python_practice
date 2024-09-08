class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        N = len(spells)
        M = len(potions)
        pairs = []

        potions.sort()

        for i in range(N):
            spell = spells[i]
            # binary search the first index of successfull pair
            left = 0
            right = M - 1
            while left <= right:
                mid = left + (right - left) // 2
                product = spell * potions[mid]
                if product >= success:
                    right = mid - 1
                else:
                    left = mid + 1
            pairs.append(M - left)
        
        return pairs

