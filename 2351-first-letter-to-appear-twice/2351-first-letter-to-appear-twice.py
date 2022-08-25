class Solution:
    def repeatedCharacter(self, s: str) -> str:
        check = set()
        for i in s:
            if i in check: return i
            check.add(i)