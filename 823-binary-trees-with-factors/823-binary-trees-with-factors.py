class Solution:
    def numFactoredBinaryTrees(self, nums: List[int]) -> int:
        nums.sort()
        limit = nums[-1]
        dic = defaultdict(int)
        # for i in nums:
        #     dic[i] += 1
        val = 0
        for i in nums:
            dic[i] += 1
            vstd = set()
            for j in range(val):
                
                if nums[j] in dic and i % nums[j] == 0 and i//nums[j] in dic and nums[j] not in vstd:
                    vstd.add(nums[j])
                    vstd.add(i//nums[j])
                    if i//nums[j] != nums[j]:
                        dic[i] += dic[nums[j]]*dic[i//nums[j]]*2
                    else:
                        dic[i] += dic[nums[j]]*dic[i//nums[j]]
            val += 1
        ans = 0
        for i in nums:
            ans += dic[i]
        return ans%(10**9+7)