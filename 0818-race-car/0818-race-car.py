class Solution:
    def racecar(self, target: int) -> int:
        start = (0,1,0)
        deq = deque([start])
        vstd = set({(0,1)})
        while deq:
            pos,speed,step = deq.popleft()
            if pos == target:
                return step
            posplus = pos + speed
            rev = 1 if speed < 0 else -1
            if (posplus,speed*2) not in vstd:
                vstd.add((posplus,speed*2))
                deq.append((posplus,speed*2,step+1))
            if (pos,rev) not in vstd:
                vstd.add((pos,rev))
                deq.append((pos,rev,step+1))
                