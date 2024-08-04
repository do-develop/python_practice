class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        def binsearch(arr, x):
            left = 0
            right = len(arr) - 1

            ans = len(arr)

            while (left <= right):
                mid = left + (right - left) // 2
                if(arr[mid] >= x):
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return ans

        htl = defaultdict(list)
        for l, h in rectangles:
            htl[h].append(l)

        for k, v in htl.items():
            v.sort() # sort by length (width)

        counts = []
        for x, y in points:
            cnt = 0

            for h in range(y, 101):
                if h in htl:
                    cnt += len(htl[h]) - binsearch(htl[h], x)
            counts.append(cnt)
        return counts
