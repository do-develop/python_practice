class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n <= 1:
            return 0
        
        total_time = 0
        employees = defaultdict(list)
        for idx, mng in enumerate(manager):
            employees[mng].append(idx)
        
        q = deque([(headID, informTime[headID])])
        while q:
            cur_id, cur_time = q.popleft()
            total_time = max(total_time, cur_time)
            for emp in employees[cur_id]:
                q.append((emp, cur_time + informTime[emp]))
        return total_time
