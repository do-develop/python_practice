class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        count = 0
        output = ['']
        for i in range(len(s)-1, -1, -1):
            if (s[i] != '-'):
                output += s[i].upper()
                count += 1
                if (count == k):
                    count = 0
                    output += '-'
        
        # output shouldn't start with a dash
        if (len(output) > 0 and output[-1] == '-'):
            output = output[:-1]  # trim the last char '-'
        output = output[::-1]
        result =  "".join(output)
        return result
