class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        wall = set()
        for i in walls:
            wall.add((i[0],i[1]))
        seen = set()
        vstd_dir = set()
        for i in guards:
            diff = 1
            if (i[0],i[1]) not in seen or (-1,i[1]) not in vstd_dir or (i[0],-1) in vstd_dir:
                while i[0]-diff>=0:
                    temp = (i[0]-diff,i[1])
                    if temp in wall:
                        break
                    seen.add(temp)
                    diff+=1
            diff = 1
            if (i[0],i[1]) not in seen or (i[0],-1) not in vstd_dir or (-1,i[1]) in vstd_dir:
                while i[1]-diff>=0:
                    temp = (i[0],i[1]-diff)
                    if temp in wall:
                        break
                    seen.add(temp)
                    diff+=1
            diff = 1
            if (i[0],i[1]) not in seen or (-1,i[1]) not in vstd_dir or (i[0],-1) in vstd_dir:
                while i[0]+diff<m:
                    temp = (i[0]+diff,i[1])
                    if temp in wall:
                        break
                    seen.add(temp)
                    diff+=1
            diff = 1
            if (i[0],i[1]) not in seen or (i[0],-1) not in vstd_dir or (-1,i[1]) in vstd_dir:
                while i[1]+diff<n:
                    temp = (i[0],i[1]+diff)
                    if temp in wall:
                        break
                    seen.add(temp)
                    diff+=1
            vstd_dir.add((i[0],-1))
            vstd_dir.add((-1,i[1]))
            seen.add((i[0],i[1]))
        return m*n-len(seen)-len(walls)