class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # union find approach
        # check if there are vertices have the same parent
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n): # find parent
            p = parent[n]
            while p != parent[p]:
                parent[p] =  parent[parent[p]] # grand-parent
                p = parent[p]
            return p
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            # found cycle
            if p1 == p2:
                return False
            # update parent and rank
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True
        
        for n1, n2 in edges:
            if not union(n1, n2):
                return [n1, n2]
