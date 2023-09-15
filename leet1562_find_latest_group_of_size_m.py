class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if m == len(arr): return m

        len_at_idx = [0] * (len(arr) + 2)
        count_len = [0] * (len(arr) + 2)
        ans = -1

        for i in range(len(arr)):
            right = len_at_idx[arr[i] + 1]
            left = len_at_idx[arr[i] - 1]
            new_len = left + right + 1
            len_at_idx[arr[i]] = new_len
            len_at_idx[arr[i] - left] = new_len
            len_at_idx[arr[i] + right] = new_len

            count_len[left] -= 1
            count_len[right] -= 1
            count_len[len_at_idx[arr[i]]] += 1

            if count_len[m] > 0:
                ans = i + 1
        
        return ans
