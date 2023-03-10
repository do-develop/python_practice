class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size + 1)]
    
    def find(self, idx): # find parent
        if idx != self.parent[idx]:
            self.parent[idx] = self.find(self.parent[idx])
        return self.parent[idx]

    # check parent conflict
    # parent of dislike node is the same as the parent of current node
    def union(self, dislike_i, parent_dislike_i, parent_i):
        p_i = self.find(dislike_i)
        self.parent[p_i] = parent_dislike_i
        return p_i != parent_i

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        self.graph = collections.defaultdict(list)
        uf = UnionFind(n)
        for (x, y) in dislikes:
            self.graph[x].append(y)
            self.graph[y].append(x)

        for node in range(1, n + 1):
            parent_node = uf.find(node)
            if parent_node in self.graph:
                parent_dislike_node = uf.find(self.graph[node][0])
                for dislike in self.graph[node][1:]:
                    if not uf.union(dislike, parent_dislike_node, parent_node):
                        return False
        return True
