class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # content map to paths
        M = collections.defaultdict(list)
        # parse the paths
        for path in paths:
            data = path.split()
            addr = data[0]
            for file in data[1:]:
                name, _, content = file.partition('(')
                M[content[:-1]].append(addr + '/' + name)
        # return the file path that has duplicate contents
        return [x for x in M.values() if len(x) > 1]
