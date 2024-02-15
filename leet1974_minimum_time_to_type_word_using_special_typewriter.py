class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        word = 'a' + word # the pointer starts from a
        for i in range(len(word) - 1):
            distance = abs(ord(word[i]) - ord(word[i + 1]))
            anti_distance = abs(distance - 26)
            time += min(distance, anti_distance)
        return time + len(word) - 1 # -1 because a was added
