class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        count = 0

        for idx, word in enumerate(words):
            valid = True
            hyphen = 0

            for i, c in enumerate(word):
                if c.isdigit():
                    valid = False
                    break
                if c in ("!", ".", ",") and i != len(word) - 1:
                    valid = False
                    break
                if (c == "-" and (i == len(word)-1 or i == 0)) or (c == "-" and (not word[i - 1].isalpha() or not word[i + 1].isalpha())):
                    valid = False
                    break
                if c == "-":
                    hyphen += 1
                    if hyphen > 1:
                        valid = False
                        break
            if valid:
                count += 1
        return count
