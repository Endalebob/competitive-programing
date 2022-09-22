class Solution:
    def reverseWords(self, s: str) -> str:
        new_s = ''
        rev_s = s.split()
        for i in rev_s:
            new_s += i[::-1]+' '
        return new_s.strip()