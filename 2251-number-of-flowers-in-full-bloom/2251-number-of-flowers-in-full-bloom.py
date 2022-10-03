class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start,end = [],[]
        for i,j in flowers:
            start.append(i)
            end.append(j)
        start.sort()
        end.sort()
        ans = []
        for i in persons:
            ans.append(bisect_right(start,i)-bisect_left(end,i))
        return ans