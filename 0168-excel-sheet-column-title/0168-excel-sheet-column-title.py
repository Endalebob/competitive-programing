class Solution:
    def convertToTitle(self, num: int) -> str:
        ans = ''
        while num:
            ans += chr(ord('A')+(num-1) % 26)
            num = (num-1) // 26
        return ans[::-1]