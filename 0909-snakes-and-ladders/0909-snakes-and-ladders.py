class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n =len(board)
        flag = n%2
        gird = []
        for i in range(n*n,0,-n):
            temp = []
            for j in range(n):
                temp.append(i-j)
            if flag:
                gird.append(temp[::-1])
            else:
                gird.append(temp)
            flag = 1-flag
        mapp = {}
        for i in range(n):
            for j in range(n):
                mapp[gird[i][j]] = board[i][j]
                
        que = deque([[1,False,0]])
        
        vstd = {(1,False)}
        while que:
            pos,flag,cost = que.popleft()
            if pos == n*n:
                return cost
            if mapp[pos] != -1:
                if flag:
                    continue
                pos = mapp[pos]
                if pos == n*n:
                    return cost
                vstd.add((pos,True))
            else:
                flag = False
            for i in range(pos+1,min(pos+7,n*n+1)):
                if (i,flag) not in vstd:
                    vstd.add((i,flag))
                    que.append([i,flag,cost+1])
                    
        return -1
                    