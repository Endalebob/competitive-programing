class Solution:
    def numSquares(self, n: int) -> int:
        deq = deque()
        first = []
        i = 1
        while i * i <= n:
            deq.append( i * i )
            first.append(i*i)
            if i*i == n:
                return 1
            i += 1
        level = 1
        while deq:
            for ii in range(len(deq)):
                curr = deq.popleft()
                i = 0
                while i<len(first) and curr + first[i] < n:
                    deq.append(curr+first[i])
                    i += 1
                if i<len(first) and curr + first[i] == n:
                    return level + 1
            level += 1
        
        
        