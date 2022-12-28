class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        cnt = 0
        vowel = {'a','i','o','e','u'}
        for i in range(len(s)):
            if i < len(s)//2:
                if s[i].lower() in vowel:
                    cnt += 1
            else:
                if s[i].lower() in vowel:
                    cnt -= 1
        return cnt == 0
            