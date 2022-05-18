"""
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as
http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work. You
just need to ensure that a URL can be encoded to a tiny URL and the tiny URL
can be decoded to the original URL.
"""

class Codec:
    def __init__(self):
        self.encodeMap = {}
        self.decodeMap = {}
        self.base = "https://tinyurl.com/"

    def encode(self, longUrl: str) -> str:
        hash_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01233456789"
        total = 0
        shorten = ""
        for c in longUrl:
            total += ord(c)
        
        while total > 0:
            shorten += hash_map[total % 62]
            total //= 62

        shortUrl = self.base + shorten

        self.encodeMap[longUrl] = shortUrl
        self.decodeMap[shortUrl] = longUrl

        return self.encodeMap[longUrl]

        
    def decode(self, shortUrl: str) -> str:
        return self.decodeMap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

url = "https://leetcode.com/problems/design-tinyurl"
obj = Codec()
tiny = obj.encode(url) # returns the encoded tiny url.
ans = obj.decode(tiny) # returns the original url after deconding it.
print(tiny)
print(ans)
