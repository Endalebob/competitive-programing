class Solution:
    def simplifyPath(self, path: str) -> str:
        splited = path.split('/')
        idx = 0
        stack = []
        while idx<=len(splited)-1:
            if splited[idx] == '..':
                if stack:
                    stack.pop()
                idx += 1
                continue
            if splited[idx] == '.' or splited[idx] == '':
                idx += 1
                continue
            temp = '/' + splited[idx]
            stack.append(temp)
            idx += 1
        ans = ''.join(stack)
        if not ans:
            return '/'
        return ans