class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        visited = [False] * len(accounts)
        email_map = defaultdict(list)
        result = []

        # build the graph
        for i, account in enumerate(accounts):
            for idx in range(1, len(account)):
                email = account[idx]
                email_map[email].append(i)
        
        # DFS to traverse all accounts
        def dfs(i, emails):
            if visited[i]:
                return
            visited[i] = True
            for idx in range(1, len(accounts[i])):
                email = accounts[i][idx]
                emails.add(email)
                for neighbor in email_map[email]:
                    dfs(neighbor, emails)
        
        # DFS for account merge
        for i, account in enumerate(accounts):
            if visited[i]:
                continue
            name, emails = account[0], set()
            dfs(i, emails)
            result.append([name] + sorted(emails))
        return result
