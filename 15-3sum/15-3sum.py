class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        ret = float('inf')
        answer = set()
        for i in range(len(nums) - 2):
            small = i + 1
            large = len(nums) - 1
            flag = True
            while large > small:
                ans = nums[i] + nums[small] + nums[large]
                if target == ans:
                    flag = False
                    answer.add((nums[i], nums[small], nums[large]))
                if target - ans > 0:
                    Flag = False
                    small += 1
                else:
                    large -= 1
            # if flag:
            #     return answer
        return answer