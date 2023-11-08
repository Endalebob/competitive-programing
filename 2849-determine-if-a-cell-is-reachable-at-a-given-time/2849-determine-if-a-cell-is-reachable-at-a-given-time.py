class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x,y = abs(sx-fx),abs(sy-fy)
        m = max(x,y)
        if (not m and t == 1) or t<m:
            return False
        return True