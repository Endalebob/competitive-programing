class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mTrue = len(nums)-1
        for idx in range(len(nums)-2,-1,-1):
            if idx + nums[idx] >= mTrue:
                mTrue = idx
        return mTrue == 0
        