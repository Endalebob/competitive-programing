class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        target_no = []
        for i in range(len(heights)-1):
            if heights[i]-heights[i+1]<0:
                target_no.append([(heights[i+1]-heights[i]),i])
        i = 0
        temp = []
        if ladders >= len(target_no):
            return len(heights)-1
        while i<ladders:
            heapq.heappush(temp,target_no[i])
            i += 1
        while bricks>0 and i<len(target_no):
            heapq.heappush(temp,target_no[i])
            bricks -= heapq.heappop(temp)[0]
            if bricks>=0:
                i += 1
            if i>=len(target_no):
                return len(heights)-1
        return target_no[i][1]