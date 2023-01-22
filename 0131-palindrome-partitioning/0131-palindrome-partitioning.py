class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def ispalindrome(ss):
            for i in range(len(ss)//2):
                if ss[i] != ss[-i-1]:
                    return False
            return True
        ans = []
        def dfs(temp,idx):
            if idx == len(s):
                if temp:
                    for i in temp:
                        if not ispalindrome(i):
                            return
                    ans.append(temp.copy())
                return
            if not temp or ispalindrome(temp[-1]):
                temp.append(s[idx])
                dfs(temp,idx+1)
                temp.pop()
            if temp:
                temp[-1] += s[idx]
                dfs(temp,idx+1)
            return ans
        return dfs([],0)
                    
                    
            