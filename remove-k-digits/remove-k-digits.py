class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        if len(num)<=k:
            return "0"
        for i in num:
            while len(stack)>0 and eval(stack[-1])>eval(i) and k>0:
                stack.pop()
                k -= 1
            stack.append(i)
        while k>0:
            stack.pop()
            k -= 1
        st = ''
        for i in stack:
            st += str(i)
        while len(st)>1 and st[0] == "0":
                 st = st[1:]
        return st