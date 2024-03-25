class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        # how many nodes in 3 branches --> DFS approach
        # graph of children to count children (left + right)
        # third branch(up) is n - left - right - 1 (self)
        children = collections.defaultdict(list)

        for node, parent in enumerate(parents):
            children[parent].append(node)

        N = len(parents)
        counter = collections.Counter()

        def count_children(node):
            product, total = 1, 0
            for child in children[node]:
                res = count_children(child)
                product *= res
                total += res
            product *= max(1, N - total - 1)
            counter[product] += 1
            return total + 1 # (children nodes + self)

        count_children(0)
        return counter[max(counter.keys())]
