class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rQue = deque()
        lQue = deque()
        length = len(senate)
        for i in range(len(senate)):
            if senate[i] == 'R':
                rQue.append(i)
            else:
                lQue.append(i)
        while rQue and lQue:
            if rQue[0]<lQue[0]:
                rQue.append(rQue.popleft()+length)
                lQue.popleft()
            else:
                rQue.popleft()
                lQue.append(lQue.popleft()+length)
        if rQue:
            return 'Radiant'
        return 'Dire'