class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def ans(l,temp,ret):
            if len(temp) == k:
                ret.append(deepcopy(temp))
                return 
            for i in range(l,n+1):
                temp.append(i)
                ans(i+1,temp,ret)
                temp.pop()
            return ret
        return ans(1,[],[])