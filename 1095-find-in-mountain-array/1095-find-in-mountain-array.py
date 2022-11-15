# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # the first step is finding the mountain
        l,r = 0,mountain_arr.length()-1
        while l<r:
            m = l + (r-l)//2
            if mountain_arr.get(m) < mountain_arr.get(m+1):
                l = m+1
            else:
                r = m
        mountain = l
        
        l,r = 0,mountain
        while l <= r:
            m = l + (r-l)//2
            val = mountain_arr.get(m)
            if val == target:
                return m
            elif val > target:
                r = m-1
            else:
                l = m+1
        l,r = mountain,mountain_arr.length()-1
        while l<=r:
            m = l + (r-l)//2
            val = mountain_arr.get(m)
            if val == target:
                return m
            elif val<target:
                r = m-1
            else:
                l = m+1
        return -1
        