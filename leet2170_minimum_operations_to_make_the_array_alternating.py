class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        even_counter, odd_counter = collections.defaultdict(int), collections.defaultdict(int)
        N = len(nums)

        for i, num in enumerate(nums):
            if i % 2 == 0:
                even_counter[num] += 1
            else:
                odd_counter[num] += 1
        
        def find_top_2(counter):
            max_num1, max_num2 = 0, 0
            max_count1, max_count2 = 0, 0

            for num, count in counter.items():
                if count > max_count1:
                    max_count2 = max_count1
                    max_num2 = max_num1
                    max_count1 = count
                    max_num1 = num
                elif count > max_count2:
                    max_count2 = count
                    max_num2 = num
            return max_num1, max_num2
        
        even1, even2 = find_top_2(even_counter)
        odd1, odd2 = find_top_2(odd_counter)

        if even1 != odd1:
            return N - (even_counter[even1] + odd_counter[odd1])
        else:
            return N - max(even_counter[even1] + odd_counter[odd2], even_counter[even2] +  odd_counter[odd1])
