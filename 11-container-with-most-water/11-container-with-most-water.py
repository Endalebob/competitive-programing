class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_incr = []
        right_incr = []
        l = len(height)-1
        ans = 0
        for i, v in enumerate(height):
            j = l-i
            if len(left_incr)==0 or v>left_incr[-1][1]:
                left_incr.append([i,v])
            if len(right_incr)==0 or height[j]>right_incr[-1][1]:
                right_incr.append([j,height[j]])
            m = 0
            a = 0
        for i in left_incr:
            for j in range(m,len(right_incr)):
                a +=1
                width = right_incr[j][0]-i[0]
                he = min(right_incr[j][1],i[1])
                ans = max(ans, (he*width))
                if he == i[1]:
                    break
                else:
                    m += 1
        return ans
                