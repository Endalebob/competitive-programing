class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        '''
        swap one by one
        '''
        nums = list(num)
        original = deepcopy(nums)
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
        ans = 0
        for i in range(len(nums)):
            if nums[i] != original[i]:
                j = i+1
                while original[j] != nums[i]:
                    j += 1
                while i < j:
                    original[j],original[j-1] = original[j-1],original[j]
                    j -= 1
                    ans += 1
        return ans
        
        