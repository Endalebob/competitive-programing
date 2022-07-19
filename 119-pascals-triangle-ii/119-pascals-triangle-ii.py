class Solution:
    def getRow(self, numRows: int) -> List[int]:
        ret = []
        for i in range(numRows+1):
            ans = []
            for j in range(i+1):
                if j == 0:
                    ans.append(1)
                elif j == i:
                    ans.append(1)
                else:
                    ans.append(ret[-1][j-1]+ret[-1][j])
            ret.append(ans)
        return ret[-1]