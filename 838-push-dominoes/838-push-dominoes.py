class Solution:
    def pushDominoes(self, d: str) -> str:
        idx = [i for i in range(len(d)) if d[i] != '.']
        ans = []
        if not idx:
            return d
        if d[idx[0]]=='L':
            for i in range(idx[0]):
                ans.append('L')
        else:
            for i in range(idx[0]):
                ans.append('.')
        for i in range(1,len(idx)):
            l = idx[i-1]; r=idx[i]
            ans.append(d[l])
            if d[l] == 'R' and d[r] == 'L':
                v = (r-l-1)//2
                for j in range(l+1,l+1+v):
                    ans.append('R')
                if (r-l) % 2 == 0:
                    ans.append('.')
                for j in range(r-1,r-1-v,-1):
                    ans.append("L")
            elif d[l] == 'L' and d[r] == "L":
                for j in range(l+1,r):
                    ans.append('L')
            elif d[l] == 'R' and d[r] == "R":
                for j in range(l+1,r):
                    ans.append('R')
            else:
                for j in range(l+1,r):
                    ans.append(d[j])
        ans.append(d[idx[-1]])
        if d[idx[-1]] == 'R':
            for i in range(len(d)-1,idx[-1],-1):
                ans.append('R')
        else:
            for i in range(len(d)-1,idx[-1],-1):
                ans.append('.')
        return ''.join(ans)