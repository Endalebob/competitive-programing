class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x:x[1])
        ans = [[events[0][1],events[0][2]]]
        ret = events[0][2]
        for i in events:
            l,r = 0,len(ans)
            mid = (l+r)//2
            while l<r:
                if ans[mid][0]>=i[0]:
                    r = mid
                if ans[mid][0]<i[0]:
                    l = mid+1
                    ret = max(ret,ans[mid][1]+i[2])
                mid = (l+r)//2
            ret = max(ret,i[2])
            if i[2]>ans[-1][-1]:
                if i[1]>ans[-1][0]:
                    ans.append([i[1],i[2]])
                else:
                    ans[-1][1] = i[2]
        return ret
                    