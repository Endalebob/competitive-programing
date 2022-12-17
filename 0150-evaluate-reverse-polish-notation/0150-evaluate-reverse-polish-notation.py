class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def op(a,b,o):
            if o == '+':
                return a+b
            elif o == '-':
                return a-b
            elif o == '*':
                return a*b
            else:
                res = a/b
                if res > 0:
                    return floor(res)
                return ceil(res)
        for i in tokens:
            if not i.isdigit() and len(i) == 1:
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(op(b,a,i))
            else:
                stack.append(i)
        return int(stack[0])
                