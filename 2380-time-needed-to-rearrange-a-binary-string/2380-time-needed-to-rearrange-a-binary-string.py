class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        s = list(s)
        curr = 0
        change = True
        while change:
            change = False
            i = 0
            while i < len(s)-1:
                if s[i] == '0' and s[i+1] == '1':
                    s[i],s[i+1] = '1','0'
                    change = True
                    i += 1
                i += 1
            curr += 1
        return curr-1
                