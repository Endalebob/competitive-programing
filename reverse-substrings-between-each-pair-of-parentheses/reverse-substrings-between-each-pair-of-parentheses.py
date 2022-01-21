class Solution:
    def reverseParentheses(self, s: str) -> str:
        open_stack = []
        close_stack = []
        new_string =''
        eq = 0
        for i, v in enumerate(s):
            if v == '(':
                open_stack.append(i-eq)
            elif v == ')':
                temp = open_stack.pop()
                mi = len(open_stack)
                new_string = new_string[:temp-mi] + new_string[temp-mi:][::-1]
                print(new_string)
                eq += 2
            else:
                new_string += v
        return new_string
                