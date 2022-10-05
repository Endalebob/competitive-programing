class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = set()
        candidates.sort()
        def dfs(path,s,idx):
            if s>target:
                return
            if s == target:
                m = tuple(deepcopy(path))
                ans.add(m)
                return
            for i in range(idx,len(candidates)):
                path.append(candidates[i])
                dfs(path,s+candidates[i],i)
                path.pop()
        dfs([],0,0)
        return ans
    