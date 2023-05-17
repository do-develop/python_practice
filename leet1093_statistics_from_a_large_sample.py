class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        mini,maxi,mode,max_freq,total_sum,total_num = float('inf'),float('-inf'),0,0,0,0
        arr = []
        for n, frq in enumerate(count):
            if frq > 0:
                mini = min(mini, n)
                maxi = max(maxi, n)
            if frq > max_freq:
                mode = n
                max_freq = frq
            total_sum += frq * n
            total_num += frq
            arr.append(total_num)
        median1 = bisect.bisect(arr, (total_num - 1) // 2)
        median2 = bisect.bisect(arr, total_num // 2)
        return [mini, maxi, total_sum/total_num, (median1 + median2)/2, mode]
            