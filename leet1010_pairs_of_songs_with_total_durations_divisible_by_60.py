class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        count_pair = 0
        counter = [0] * 60
        for t in time:
            rem = t % 60
            count_pair += counter[60 - rem] if rem > 0 else counter[0]
            counter[rem] += 1
        return count_pair
