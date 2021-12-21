Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution:
    def op(self,a,b,c):
        if a == '+':
            return int(b) + int(c)
        if a == '-':
            return int(c) - int(b)
        if a == '*':
            return int(b) * int(c)
        if a == '/':
            return int(int(c) / int(b))     
    def evalRPN(self, tokens: List[str]) -> int:
        que = []
        for i in tokens:
            if i not in '+-*/' or len(i) != 1:
                que.append(i)
            else:
                m = self.op(i,que.pop(),que.pop())
                que.append(m)
        return que[0]