class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left,right,middile = [],[],[]
        for i in nums:
            if i<pivot:
                left.append(i)
            elif i>pivot:
                right.append(i)
            else:
                middile.append(i)
        return left+middile+right
        