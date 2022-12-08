class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        found = []
        row1 = 'qwertyuiop'
        row2='asdfghjkl'
        row3='zxcvbnm'

        for word in words:
            isInRow = True
            first_char = word[0].lower()
            if first_char in row1:
                row = row1
            elif first_char in row2:
                row = row2
            else:
                row = row3
            
            for c in list(word.lower()):
                if c not in row:
                    isInRow = False
                    break
            if isInRow:
                found.append(word)
                
        return found
