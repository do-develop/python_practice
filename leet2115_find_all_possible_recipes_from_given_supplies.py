class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Graph problem - use topological sort
        available = set(supplies)
        ans, ing_to_recipe, in_degree = [], defaultdict(set), Counter()

        for rcp, ingredient in zip(recipes, ingredients):
            non_avail = 0
            for ing in ingredient:
                if ing not in available:
                    non_avail += 1
                    ing_to_recipe[ing].add(rcp)
            if non_avail == 0:
                ans.append(rcp)
            else:
                in_degree[rcp] = non_avail
        
        for rcp in ans:
            for rcp in ing_to_recipe.pop(rcp, set()):
                in_degree[rcp] -= 1
                if in_degree[rcp] == 0:
                    ans.append(rcp)
        return ansv
