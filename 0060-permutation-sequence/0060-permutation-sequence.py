class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [str(i) for i in range(1,n+1)]
        k -= 1
        def perm():
            idx1 = 0
            n = len(nums)
            for i in range(n-2,-1,-1):
                if nums[i] < nums[i+1]:
                    idx1 = i
                    break
                    
            idx2 = 0
            for i in range(n-1,0,-1):
                if nums[i] > nums[idx1]:
                    idx2 = i
                    break
            nums[idx1],nums[idx2] = nums[idx2],nums[idx1]
            nums[idx1+1:] = nums[idx1+1:][::-1]
                
        
        while k:
            perm()
            k -= 1
        return ''.join(nums)
        