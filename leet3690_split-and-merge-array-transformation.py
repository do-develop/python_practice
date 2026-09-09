class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)

        if N < 3: return int(nums1 != nums2)
        if nums1 == nums2:
            return 0

        # tuples are hashable and compare by value
        nums2 = tuple(nums2)
        # (arrangement, number_of_ops_so_far)
        queue = deque([(nums1, 0)])
        # the set of arrangements already visited
        seen = set(tuple(nums1))

        while queue:
            nums1, ops = queue.popleft()
            # every pair (left, rght) with 0 <= left < rght <= n
            for left, right in combinations(range(N + 1), 2):
                # using Python slice syntax *
                removed, remains = nums1[left:right], [*nums1[:left], *nums1[right:]]
                # every valid insertion index
                for mid in range(N - right + left + 1):
                    candidate = (*remains[:mid], *removed, *remains[mid:])
                    if candidate in seen: continue
                    if candidate != nums2:
                        seen.add(candidate)
                        queue.append((candidate, ops + 1))
                    
                    else:
                        return ops + 1
