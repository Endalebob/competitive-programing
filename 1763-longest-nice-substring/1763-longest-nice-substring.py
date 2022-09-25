class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        ii = len(s)
        add = ord('a')-ord('A')
        while ii > 1:
            for i in range(len(s)-ii+1):
                check = set()
                ss = s[i:ii+i]
                for i in ss:
                    check.add(i)
                stack = []
                for i in range(len(ss)):
                    if ord(ss[i]) < ord('a'):
                        if chr(ord(ss[i])+add) not in check:
                            stack.append(i)
                    else:
                        if chr(ord(ss[i])-add) not in check:
                            stack.append(i)
                if not stack:
                    return ss
            ii -= 1
        return ''