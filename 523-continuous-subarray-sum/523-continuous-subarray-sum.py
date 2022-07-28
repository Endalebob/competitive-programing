class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        a = 0
        pre_sum = []
        for i in range(len(nums)):
            pre_sum.append(a + nums[i])
            a += nums[i]
        rem = set()
        a = 0 if pre_sum[0]%k != 0 else 1
        for i in range(a,len(pre_sum)):
            if pre_sum[i]%k == 0 or (pre_sum[i]%k in rem and pre_sum[i]%k != pre_sum[i-1]%k) or (nums[i]%k == 0 and nums[i-1]%k==0):
                return True
            rem.add(pre_sum[i]%k)
        return False