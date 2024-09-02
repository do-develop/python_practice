class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split()
        rate = discount / 100
        res = []

        for word in words:
            if word[0] != '$' or word[1:].isdigit() == False:
                res.append(word)
            else:
                price = int(word[1:])
                discounted_price = price * (1 - rate)
                res.append('$' + format(discounted_price, ".2f"))
        
        return ' '.join(res)
