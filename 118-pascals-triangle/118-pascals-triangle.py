class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            ans = []
            for j in range(i+1):
                if j == 0:
                    ans.append(1)
                elif j == i:
                    ans.append(1)
                else:
                    ans.append(ret[-1][j-1]+ret[-1][j])
            ret.append(ans)
        return ret