class Solution:
    def decodeString(self, s: str) -> str:
        idx = 0
        def decoder():
            nonlocal idx
            st,num = '',''
            while idx < len(s) and s[idx] != ']':
                if s[idx].isalpha():
                    st += s[idx]
                elif s[idx].isdigit():
                    num += s[idx]
                else:
                    idx += 1
                    st += decoder() * int(num)
                    
                    num = ''
                idx += 1
            return st
        return decoder()