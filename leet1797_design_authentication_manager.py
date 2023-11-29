class AuthenticationManager:
    # FIFO nature, use queue
    def __init__(self, timeToLive: int):
        self.tokens = collections.OrderedDict()
        self.ttl = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self._evict(currentTime)
        self.tokens[tokenId] = currentTime + self.ttl # put new keys at the tail (the newest)

    def _evict(self, currentTime:int) -> int:
        while self.tokens and  next(iter(self.tokens.values())) <= currentTime:
            self.tokens.popitem(last=False)

    def renew(self, tokenId: str, currentTime: int) -> None:
        self._evict(currentTime)
        if tokenId not in self.tokens:
            return
        self.tokens.move_to_end(tokenId)
        self.tokens[tokenId] = currentTime + self.ttl

    def countUnexpiredTokens(self, currentTime: int) -> int:
        self._evict(currentTime)
        return len(self.tokens)


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)
