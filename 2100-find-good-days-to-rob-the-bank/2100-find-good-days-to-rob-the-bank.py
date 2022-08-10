class Solution:
    def goodDaysToRobBank(self, nums: List[int], time: int) -> List[int]:
        incr,decr = [1],[1]
        for i in range(1,len(nums)):
            if nums[i]>= nums[i-1]:
                incr.append(incr[-1]+1)
            else:
                incr.append(1)
            
            if nums[i]<= nums[i-1]:
                decr.append(decr[-1]+1)
            else:
                decr.append(1)
        ans = []
        for i in range(time,len(nums)-time):
            if incr[i+time]-incr[i] >= time and decr[i]-decr[i-time] >= time:
                ans.append(i)
        return ans
            