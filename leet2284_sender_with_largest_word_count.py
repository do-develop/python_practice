class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        counter = defaultdict(int)
        for msg, sender in zip(messages, senders):
            counter[sender] += len(msg.split())
        
        return max(counter, key=lambda k: (counter[k], k))
