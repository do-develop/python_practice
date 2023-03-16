class Solution:
# sliding window approach
    def totalFruit(self, fruits: List[int]) -> int:
        # basket to store the types of fruits
        basket = {}
        left = 0

        # add fruit from the right idx of the window
        for right, fruit in enumerate(fruits):
            basket[fruit] = basket.get(fruit, 0) + 1
            # can't have more than 2 types of fruit
            if len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
        # size of the biggest subarray
        return right - left + 1
