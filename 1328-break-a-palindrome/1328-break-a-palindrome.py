class Solution:
    def breakPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return ''
        m = len(s)//2
        temp = 0
        for i in range(m):
            temp = i
            if s[i] > 'a':
                break
        if s[temp] == 'a':
            # if s[temp+1] != 'a':
            #     return s[:temp+1] + 'a' + s[temp+2:]
            return s[:-1] + 'b'
        return s[:temp] + 'a' + s[temp+1:]
            