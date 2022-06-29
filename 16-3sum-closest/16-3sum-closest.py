class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ret = float('inf')
        for i in range(len(nums) - 2):
            flag = True
            small = i + 1
            large = len(nums) - 1
            while large > small:
                ans = nums[i] + nums[small] + nums[large]
                if target == ans:
                    return ans
                if abs(target-ans)<abs(target-ret):
                    ret = ans
                if target - ans > 0:
                    flag = False
                    small += 1
                else:
                    large -= 1
            if flag:
                return ret
        return ret