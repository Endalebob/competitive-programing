class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(clo,ope,s):
            if ope == 0:
                ans.append(s)
            if ope > clo:
                backtrack(clo,ope-1,s+')')
            if clo > 0:
                backtrack(clo-1,ope,s+'(')
        backtrack(n,n,'')
        return ans