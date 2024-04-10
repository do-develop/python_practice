class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        # length of encoded string = rows * cols
        # s[i] and s[i + cols + 1] adjecent to each other
        N = len(encodedText)
        cols = len(encodedText) // rows
        decoded = []
        for i in range(cols):
            while i < N:
                decoded.append(encodedText[i])
                i += (cols + 1)
        return ''.join(decoded).rstrip()
