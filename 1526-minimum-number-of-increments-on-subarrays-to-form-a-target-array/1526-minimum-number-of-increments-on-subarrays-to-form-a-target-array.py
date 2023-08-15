class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = 0
        curr = 0
        for i in target:
            ans += max(0,i-curr)
            curr = i
        return ans