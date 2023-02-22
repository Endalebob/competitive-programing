class Solution:
    def calculate(self, s: str) -> int:
        sign = 1
        stack = []
        res = 0
        num = ''
        for i in s:
            if i.isdigit():
                num += i
            elif i in { '+' ,'-'}:
                if num:
                    res += sign*int(num)
                    
                sign = 1 if i == '+' else -1
                num = ''
            elif i == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif i == ')':
                if num:
                    res += sign*int(num)
                s = stack.pop()
                val = stack.pop()
                res *= s
                res += val
                num = ''
        if num:
            return res + int(num)*sign
        return res