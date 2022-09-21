class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        def perm(s):
            if len(s) == n:
                ans.append(s)
                return
            for i in ["a", "b", "c"]:
                if s and s[-1] == i:
                    continue
                perm(s+i)
        perm('')
        if len(ans)>=k:
            ans.sort()
            return ans[k-1]
        return ''