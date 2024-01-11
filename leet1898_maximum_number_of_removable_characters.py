class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_possible(k):
            str_arr = list(s)
            for i in removable[:k]:
                str_arr[i] = ''
            return is_subsequence(p, str_arr)

        def is_subsequence(substr, target):
            target = iter(target)
            return all(c in target for c in substr)
            
        # bianry search approach
        l, r = 0, len(removable)

        while l < r:
            k = (l + r + 1) // 2
            if is_possible(k):
                l = k
            else:
                r = k - 1
        return l
