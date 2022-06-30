class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = defaultdict(list)
        for i,v in enumerate(nums):
            dic[v].append(i)
        check = list(dic.values())
        ans = k+1
        for i in check:
            for j in range(len(i)-1):
                ans = min(ans,i[j+1]-i[j])
            if ans<=k:
                return True
        return ans<=k