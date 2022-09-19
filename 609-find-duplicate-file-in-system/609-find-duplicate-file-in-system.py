class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for i in paths:
            a = i.split()
            for j in a[1:]:
                c,d = j.split('(')
                dic[d].append(a[0]+'/'+c)
        ans = []
        for i in dic:
            if len(dic[i])>1:
                ans.append(dic[i])
        return ans