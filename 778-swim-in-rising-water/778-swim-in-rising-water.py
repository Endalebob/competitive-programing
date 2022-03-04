class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        row = len(grid)
        isValid = lambda r,c: 0<=r<row and 0<=c<row
        neghibour = [[0,1],[0,-1],[1,0],[-1,0]]
        checked = set()
        checked.add((0,0))
        deq = []
        heapq.heappush(deq,[grid[0][0],0,0])
        ans = 10000
        while deq:
            current = heapq.heappop(deq)
            for i in neghibour:
                if isValid(current[1]+i[0],current[-1]+i[1]):
                    if (current[1]+i[0],current[-1]+i[1]) not in checked:
                        if grid[current[1]+i[0]][current[-1]+i[1]]<current[0]:
                            checked.add((current[1]+i[0],current[-1]+i[1]))
                            heapq.heappush(deq,[current[0],current[1]+i[0],current[-1]+i[1]])
                        else:
                            checked.add((current[1]+i[0],current[-1]+i[1]))
                            heapq.heappush(deq,[grid[current[1]+i[0]][current[-1]+i[1]],current[1]+i[0],current[-1]+i[1]])  
            if current[1] == row-1 and current[-1] == row-1:
                ans = min(ans,current[0])
                return ans
        return ans