# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        right = mountain_arr.length()-1
        def find_pick():
            l,r = 0, right
            while l<r:
                mid = l + (r-l)//2
                if mountain_arr.get(mid-1) < mountain_arr.get(mid) < mountain_arr.get(mid+1):
                    l = mid
                elif mountain_arr.get(mid-1) > mountain_arr.get(mid) > mountain_arr.get(mid+1):
                    r = mid
                else:
                    return mid
        pick = find_pick()
        
        def find_left_most(l,r):
            while l<r:
                mid = l + (r-l)//2
                if mountain_arr.get(mid) >= target:
                    r = mid
                else:
                    l = mid+1
            return l if mountain_arr.get(l) == target else -1
        def find_leftt_most(l,r):
            while l<r:
                mid = l + (r-l)//2
                if mountain_arr.get(mid) <= target:
                    r = mid
                else:
                    l = mid+1
            return l if mountain_arr.get(l) == target else -1
        ans = find_left_most(0,pick)
        if ans != -1:
            return ans
        return find_leftt_most(pick,right)