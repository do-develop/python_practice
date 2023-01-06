class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n

        def normalize_process(process_time):
            return process_time.split(':')

        for process in logs:
            pid, event_type, time = normalize_process(process)
            if event_type == "start":
                stack.append([pid, time])
            elif event_type == "end":
                pid, start_time = stack.pop()
                spent_time = int(time) - int(start_time) + 1 # add 1, cause 0 is included
                result[int(pid)] += spent_time
                # decrement time for the next process in the stack
                if len(stack) != 0:
                    next_pid, next_time = stack[-1]
                    result[int(next_pid)] -= spent_time
        return result
