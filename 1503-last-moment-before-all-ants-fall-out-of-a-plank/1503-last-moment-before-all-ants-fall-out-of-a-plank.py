class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        if left and right:
            return max(max(left),n-min(right))
        if left:
            return max(left)
        return n-min(right)