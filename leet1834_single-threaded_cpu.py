class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        N = len(tasks)
        idx = 0
        for task in tasks:
            task.append(idx)
            idx += 1
        tasks.sort()

        heap = []
        idx = 0
        arrival = tasks[0][0]
        while idx < N:
            if tasks[idx][0] == arrival:
                heapq.heappush(heap, [tasks[idx][1], tasks[idx][2]])
            else:
                break
            idx += 1
        
        order = []
        while (heap):
            start_time, process_time = heapq.heappop(heap)
            order.append(process_time)
            arrival += start_time
            # for this arrival time add the tasks in min heap
            while (idx < N and tasks[idx][0] <= arrival):
                heapq.heappush(heap, [tasks[idx][1], tasks[idx][2]])
                idx += 1

            # when there is an idle time
            if not heap and idx < N:
                # move the arrival time to the next task start time
                arrival = tasks[idx][0]
                while (idx < N):
                    if tasks[idx][0] == arrival:
                        heapq.heappush(heap, [tasks[idx][1], tasks[idx][2]])
                    else:
                        break
                    idx += 1
        return order
