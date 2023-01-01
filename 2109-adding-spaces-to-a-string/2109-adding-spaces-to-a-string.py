class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        idx = 0
        ans = ''
        for i in range(len(s)):
            if idx < len(spaces) and i == spaces[idx]:
                ans += ' '
                idx += 1
            ans += s[i]
        return ans