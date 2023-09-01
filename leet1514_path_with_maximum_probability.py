class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Bellman-Ford Algorithm
        # only need to repeat n - 1 times

        max_prob = [0] * n
        max_prob[start_node] = 1

        for i in range(n - 1):
            has_update = False
            for j in range(len(edges)):
                s, e = edges[j]
                path_prob = succProb[j]
                if max_prob[s] * path_prob > max_prob[e]:
                    max_prob[e] = max_prob[s] * path_prob
                    has_update = True
                if max_prob[e] * path_prob > max_prob[s]:
                    max_prob[s] = max_prob[e] * path_prob
                    has_update = True
            if not has_update:
                break
        return max_prob[end_node]
