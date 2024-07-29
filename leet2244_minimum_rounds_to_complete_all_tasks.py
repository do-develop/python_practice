class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = defaultdict(int)
        N = len(tasks)

        for i in range(N):
            freq[tasks[i]] += 1
        
        rounds = 0
        for _, frequency in freq.items():
            if frequency < 2:
                return -1
            
            rounds += math.ceil(frequency/3)
        return rounds
