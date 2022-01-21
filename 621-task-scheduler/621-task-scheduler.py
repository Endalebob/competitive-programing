class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        se = set(tasks)
        m = tasks.count('A')
        li = []
        if n == 0:
            return len(tasks)
        for i in se:
            li.append(tasks.count(i))
        c = max(li)
        if len(tasks) < c*(n+1) - (n-li.count(c)+1):
            return c*(n+1) - (n-li.count(c)+1)
        return len(tasks)
            
        