import bisect
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        dic = defaultdict(list)
        for key,value in people:
            bisect.insort(dic[key],value)
        keys = list(dic.keys())
        keys.sort(reverse = True)
        ans = []
        for i in keys:
            for j in dic[i]:
                ans.insert(j,[i,j])
        return ans