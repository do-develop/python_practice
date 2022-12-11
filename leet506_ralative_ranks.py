class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        size = len(score)
        output = [''] * size
        pos = {}

        # remember the original position
        for i in range(size):
            pos[score[i]] = i

        # sort in descending order
        score.sort(reverse=True)

        for i in range(size):
            if i < 3:
                output[pos[score[i]]] = medals[i]
            else:
                output[pos[score[i]]] = str(i + 1)
        
        return output
