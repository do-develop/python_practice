class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        tokens = s.split()
        prev = -1
        for word in tokens:
            if word.isnumeric():
                curr = int(word)
                if curr > prev:
                    prev = curr
                else:
                    return False
        return True
