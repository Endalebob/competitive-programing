class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1).intersection(set(list2))
        dic1,dic2 = {},{}
        for i in range(len(list1)):
            dic1[list1[i]] = i
        for i in range(len(list2)):
            dic2[list2[i]] = i
        minn = 122222222
        ans = []
        for i in common:
            minn = min(minn,dic1[i]+dic2[i])
        for i in common:
            if dic1[i]+dic2[i] == minn:
                ans.append(i)
        return ans
        
            