class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def generator(s):
            ans = []
            for idx in range(4):
                temp = s[idx]
                if int(s[idx]) == 0:
                    ans.append(s[:idx]+'9'+s[idx+1:])
                else:
                    ans.append(s[:idx]+str(int(s[idx])-1)+s[idx+1:])
                if int(s[idx]) == 9:
                    ans.append(s[:idx]+'0'+s[idx+1:])
                else:
                    ans.append(s[:idx]+str(int(s[idx])+1)+s[idx+1:])
                
            return ans
        
        vstd = {'0000'}
        deadends = set(deadends)
        if '0000' in deadends:
            return -1
        deq = deque([['0000',0]])
        while deq:
            curr = deq.popleft()
            if curr[0] == target:
                    return curr[1]
            for i in generator(curr[0]):
                if i not in vstd and i not in deadends:
                    vstd.add(i)
                    deq.append([i,curr[1]+1])
                    if i == target:
                        return curr[1]+1
        return -1
                
                