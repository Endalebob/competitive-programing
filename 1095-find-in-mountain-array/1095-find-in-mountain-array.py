# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        #the first step is to find the mountain
        l,r = 0,mountain_arr.length()-1
        if r < 2:
            return -1
        while l < r:
            m = l + (r-l)//2
            if mountain_arr.get(m) < mountain_arr.get(m+1):
                l = m+1
            else:
                r = m
        
        #check in the first part
        val = l
        r = val
        l = 0
        while l <= r:
            m = l + (r-l)//2
            if mountain_arr.get(m) == target:
                return m
            if mountain_arr.get(m) > target:
                r = m -1
            else:
                l = m + 1
        
        #second check
        
        l = val+1
        r = mountain_arr.length()-1
        while l <= r:
            m = l + (r-l)//2
            if mountain_arr.get(m) == target:
                return m
            if mountain_arr.get(m) < target:
                r = m -1
            else:
                l = m + 1 
        return -1