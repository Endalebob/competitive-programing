class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vstd = set()
        dic = defaultdict(list)
        for i in range(len(nums)):
            dic[nums[i]].append(i)
        for i in nums:
            if target-i in vstd:
                return [dic[target-i][0],dic[i][-1]]
            vstd.add(i)
            