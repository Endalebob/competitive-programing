class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []
        supplies = set(supplies)
        l = len(supplies) + len(recipes)
        while True:
            m = len(ans)
            for i in range(len(recipes)):
                if recipes[i] not in supplies:
                    flag = True
                    for j in ingredients[i]:
                        if j not in supplies:
                            flag = False
                            break
                    if flag:
                        supplies.add(recipes[i])
                        ans.append(recipes[i])
            if m == len(ans):
                break
        return ans