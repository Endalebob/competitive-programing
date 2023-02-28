class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        start_end = {}
        for i in range(len(nums)):
            if nums[i] in start_end:
                start_end[nums[i]][1] = i+1
            else:
                start_end[nums[i]] = [i,i+1]
        ans = [1,len(nums)]
        for i in count:
            if count[i] > ans[0]:
                ans = [count[i],start_end[i][1]-start_end[i][0]]
            elif count[i] == ans[0] and ans[1] > start_end[i][1]-start_end[i][0]:
                ans[1] = start_end[i][1]-start_end[i][0]
        return ans[1]
                
        
        