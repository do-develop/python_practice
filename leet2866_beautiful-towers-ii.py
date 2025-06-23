class Solution:
    def maximumSumOfHeights(self, maxHeights: List[int]) -> int:
        def find_peak(arr):
            stack, accSum = [], 0
            peeks = []

            for height in arr:
                count = 1
                while stack and height <= stack[-1][0]:
                    h, c = stack.pop()
                    accSum -= h * c
                    count += c
                stack.append((height, count))
                accSum += height * count
                peeks.append(accSum)
            return peeks


        forward = [0] + find_peak(maxHeights)
        reverse = find_peak(maxHeights[::-1])[::-1] + [0]

        return max(fwd + rvs for fwd, rvs in zip(forward, reverse))