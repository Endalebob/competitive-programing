class Solution:
    def isRobotBounded(self, ins: str) -> bool:
        x,y = 0,0
        idx = 0
        dirc = [[0,1],[1,0],[0,-1],[-1,0]]
        for i in ins:
            if i == 'R':
                idx += 1
            elif i == 'L':
                idx -= 1
            else:
                x += dirc[idx%4][0]
                y += dirc[idx%4][1]
        return idx%4 != 0 or (x,y) == (0,0)