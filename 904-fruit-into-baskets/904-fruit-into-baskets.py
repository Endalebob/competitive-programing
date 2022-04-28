class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        dic = {}
        deq = deque()
        start = 0
        ans = 0
        for i,v in enumerate(fruits):
            if len(deq) == 2 and v not in deq:
                a = deq.popleft()
                start = dic.pop(a) + 1
            ans = max(ans,i-start+1)
            if v not in deq:
                deq.append(v)
            elif deq[0] == v and len(deq) == 2:
                deq[0], deq[1] = deq[1], deq[0]
            dic[v] = i
        return ans