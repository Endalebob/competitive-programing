class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = []
        for i in s:
            if i.isalnum():
                new.append(i.lower())
        for i in range(len(new)//2):
            if new[i] != new[-i-1]:
                return False
        return True