class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = dividend//divisor
        if ans<0:
            divisor*=-1
            ans = dividend//divisor
            ans *= -1
        if ans<-(2**31):
            return -(2**31)
        elif ans>2**31-1:
            return 2**31-1
        return ans