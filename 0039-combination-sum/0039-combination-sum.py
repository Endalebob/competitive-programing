class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(path,s,idx):
            if s>target or idx>=len(candidates):
                return
            if s == target:
                ans.append(deepcopy(path))
                return
            path.append(candidates[idx])
            dfs(path,s+candidates[idx],idx)
            path.pop()
            dfs(path,s,idx+1)
        dfs([],0,0)
        return ans
    