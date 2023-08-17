class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        ans = []
        sets = [set(companies) for companies in favoriteCompanies]
        for idx1, set1 in enumerate(sets):
            for idx2, set2 in enumerate(sets):
                if idx1 == idx2:
                    continue
                if set1.issubset(set2):
                    break
            else:
                ans.append(idx1)
        return ans
