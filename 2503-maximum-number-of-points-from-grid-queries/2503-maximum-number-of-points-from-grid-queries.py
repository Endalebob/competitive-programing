class Solution:
    def maxPoints(self, grid: List[List[int]], q: List[int]) -> List[int]:
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        m,n = len(grid),len(grid[0])
        isvalid = lambda r,c : 0<=r<m and 0<=c<n
        modified = [[q[i],i] for i in range(len(q))]
        modified.sort()
        heap = [(grid[0][0],0,0)]
        heapq.heapify(heap)
        i = 0
        cnt = 0
        ans = [0]*len(q)
        vstd = set()
        while i<len(q):
            while heap and modified[i][0] > heap[0][0]:
                v,ii,j = heapq.heappop(heap)
                if (ii,j) in vstd:
                    continue
                vstd.add((ii,j))
                cnt += 1
                for r,c in dirc:
                    ni,nj = r+ii,j+c
                    if isvalid(ni,nj) and (ni,nj) not in vstd:
                        heapq.heappush(heap,(grid[ni][nj],ni,nj))
            ans[modified[i][1]] = cnt
            i += 1
        return ans