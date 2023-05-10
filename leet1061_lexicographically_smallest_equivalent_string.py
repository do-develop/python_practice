class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # union find approach
        UF = {}
        def find(x):
            UF.setdefault(x, x)
            if x != UF[x]:
                UF[x] = find(UF[x]) # find the root and set is as parent
            return UF[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)
            # make sure the root of a group is the smallest element in the group
            if rootx > rooty:
                UF[rootx] = rooty
            else:
                UF[rooty] = rootx

        # union the two equivalent strings   
        for i in range(len(s1)):
            union(s1[i], s2[i])
        # now simply find the root of the group
        res = []
        for c in baseStr:
            res.append(find(c))
        return ''.join(res)
