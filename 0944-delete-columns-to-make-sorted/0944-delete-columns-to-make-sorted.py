class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        ans = 0
        for i in range(len(strs[0])):
            small = 'a'
            for j in range(len(strs)):
                if strs[j][i] < small:
                    ans += 1
                    break
                small = strs[j][i]
        return ans