class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        if queryIP.count('.') == 3:
            return self.validate_IPv4(queryIP)
        if queryIP.count(':') == 7:
            return self.validate_IPv6(queryIP)
        else:
            return "Neither"
        
        
    def validate_IPv4(self, IP: str) -> str:
        nums = IP.split('.')
        for n in nums:
            if len(n) == 0 or len(n) > 3:
                return "Neither"
            # no extra leading zero
            # is it digit
            # is it less than 255
            if n[0] == '0' and len(n) != 1 or not n.isdigit() or int(n) > 255:
                return "Neither"
        return "IPv4"
    
    def validate_IPv6(self, IP: str) -> str:
        nums = IP.split(':')
        hexdigits = '0123456789abcdefABCDEF'
        for n in nums:
            # validate range (0, 2 ** 16)
            # at least one and not more than 4 hexdigit
            # only hexdigit allowed
            if len(n) == 0 or len(n) > 4 or not all(c in hexdigits for c in n):
                return "Neither"
        return "IPv6"
