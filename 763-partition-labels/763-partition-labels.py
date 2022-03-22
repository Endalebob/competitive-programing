class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = {}
        ans = []
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]][1] = i
            else:
                dic[s[i]] = [i,i]
        heap = list(dic.values())
        heapq.heapify(heap)
        temp = heapq.heappop(heap)
        minn,maxx = temp[0],temp[1]
        while heap:
            temp = heapq.heappop(heap)
            if temp[0]>maxx:
                ans.append(maxx-minn+1)
                minn,maxx = temp[0],temp[1]
                continue
            if temp[1]>maxx:
                maxx = temp[1]
        ans.append(maxx-minn+1)
        return ans