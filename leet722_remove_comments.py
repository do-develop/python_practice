class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result, buffer, isBlock = [], '', False
        for line in source:
            i, length = 0, len(line)
            while i < length:
                # check line comment
                if i - 1 < length and line[i:i+2] == "//" and not isBlock:
                    break # can skip this line
                # check start of the block comment
                elif i - 1 < length and line[i:i+2] == "/*" and not isBlock:
                    isBlock = True
                    i += 1
                # check end of the block comment
                elif i - 1 < length and line[i:i+2] == "*/" and isBlock:
                    isBlock = False
                    i += 1
                elif not isBlock:
                    buffer += line[i]
                i += 1
            if buffer and not isBlock:
                result.append(buffer)
                buffer = "" # reset for next round
        return result
