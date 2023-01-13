class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        for ii in range(left,right+1):
            flag = True
            for i,j in ranges:
                if i<=ii<=j:
                    flag = False
                    break
            if flag:
                return False
        return True