class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        square = [i**2 for i in nums]
        square.sort()
        return square