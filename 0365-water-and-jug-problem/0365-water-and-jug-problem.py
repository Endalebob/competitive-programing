class Solution:
    def canMeasureWater(self, j1: int, j2: int, tc: int) -> bool:
        deq = deque([(0,0)])
        vstd = set()
        while deq:
            a,b = deq.popleft()
            if a == tc or b == tc or a+b == tc:
                return True
            #state 1
            if b < j2 and a > 0:
                c = min(a,j2-b)
                if (a-c,b+c) not in vstd:
                    vstd.add((a-c,b+c))
                    deq.append((a-c,b+c))
            if a < j1 and b > 0:
                c = min(b,j1-a)
                if (a+c,b-c) not in vstd:
                    vstd.add((a+c,b-c))
                    deq.append((a+c,b-c)) 
            #state 2
            if b != 0 and (a,0) not in vstd:
                vstd.add((a,0))
                deq.append((a,0))
            if a != 0 and (0,b) not in vstd:
                vstd.add((0,b))
                deq.append((0,b))
            
            #state 3
            if b != j2 and (a,j2) not in vstd:
                vstd.add((a,j2))
                deq.append((a,j2))
            if a != j1 and (j1,b) not in vstd:
                vstd.add((j1,b))
                deq.append((j1,b))
        return False