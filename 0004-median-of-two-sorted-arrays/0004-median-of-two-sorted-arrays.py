class Solution:
    def findMedianSortedArrays(self, n: List[int], m: List[int]) -> float:
        new = n+m
        new.sort()
        rem = len(new) % 2
        idx = len(new)//2
        if rem:
            return new[idx]
        return (new[idx]+new[idx-1])/2