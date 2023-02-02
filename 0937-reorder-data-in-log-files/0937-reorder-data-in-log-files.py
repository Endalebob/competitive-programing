class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        loog = []
        for i in logs:
            loog.append(i.split())
        ans = {loog[i][0]+"%"+str(i):loog[i] for i in range(len(loog))}
        log_value = {loog[i][0]+"%"+str(i):loog[i][1:] for i in range(len(loog)) if loog[i][1][0].isdigit() == False}
        m = sorted(log_value,key = lambda x : (log_value[x],x))
        for i in range(len(loog)):
            if loog[i][1][0].isdigit():
                m.append(loog[i][0]+"%"+str(i))
        answer = []
        print(m)
        for i in m:
            answer.append(' '.join(ans[i]))
        return answer
            
        