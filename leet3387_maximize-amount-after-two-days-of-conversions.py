class Solution:
    def maxAmount(self, initialCurrency: str, pairs1: List[List[str]], rates1: List[float], pairs2: List[List[str]], rates2: List[float]) -> float:
        
        def build_graph(pairs, rates):
            graph = defaultdict(list)
            for (u, v), r in zip(pairs, rates):
                graph[u].append((v, r))
                graph[v].append((u, 1 / r))
            return graph
        
        graph1 = build_graph(pairs1, rates1)
        graph2 = build_graph(pairs2, rates2)

        def max_product(start, graph):
            best = defaultdict(float)
            best[start] = 1.0

            queue = deque([start])
            while queue:
                curr = queue.popleft()

                for nei, rate, in graph[curr]:
                    new_amount = best[curr] * rate

                    if new_amount > best[nei]:
                        best[nei] = new_amount
                        queue.append(nei)
            return best
        
        day1_best = max_product(initialCurrency, graph1)
        max_result = 0.0

        for currency, amt in day1_best.items():
            day2_best = max_product(currency, graph2)

            if initialCurrency in day2_best:
                final_amount = amt * day2_best[initialCurrency]
                max_result = max(max_result, final_amount)
        
        return max_result
