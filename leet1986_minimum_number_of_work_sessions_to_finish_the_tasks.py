class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        N = res = len(tasks)
        tasks.sort(reverse=True)
        sessions = []

        def dfs(i):
            nonlocal res
            if len(sessions) > res:
                return
            if i == N:
                res = len(sessions)
                return
            for j in range(len(sessions)):
                if sessions[j] + tasks[i] <= sessionTime:
                    sessions[j] += tasks[i]
                    dfs(i + 1)
                    sessions[j] -= tasks[i]
            # create a new session with this task
            sessions.append(tasks[i])
            dfs(i + 1)
            # backtrack the new session created to find alternative way
            sessions.pop()

        dfs(0)
        return res
