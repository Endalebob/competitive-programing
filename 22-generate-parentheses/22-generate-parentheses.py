class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def generator(par = [],l=0,r=0):
            if len(par) == 2*n:
                ans.append(''.join(par))
                return
            if l<n:
                par.append('(')
                generator(par,l+1,r)
                par.pop()
            if r<l:
                par.append(')')
                generator(par,l,r+1)
                par.pop()
        generator()
        return ans