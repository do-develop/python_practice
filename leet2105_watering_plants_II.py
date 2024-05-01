class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        N = len(plants)
        refill = 0
        left, right = 0, N - 1
        alice, bob = capacityA, capacityB

        while left <= right:
            
            if left == right:
                if alice >= bob:
                    if alice < plants[left]:
                        refill += 1
                    left += 1
    
                else:
                    if bob < plants[right]:
                        refill += 1
                    right -= 1 
            else:
                # Alice side
                if plants[left] > alice:
                    refill += 1
                    alice = capacityA
                alice -= plants[left]
                left += 1
                # Bob side
                if plants[right] > bob:
                    refill += 1
                    bob = capacityB
                bob -= plants[right]
                right -= 1
        return refill
