class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        idxs = defaultdict(list)
        for i,j in enumerate(s): idxs[j].append(i)
        ans = 0
        for i in words:
            start = -1
            flag = True
            for k in i:
                if k not in idxs or start > idxs[k][-1]:
                    flag = False
                    break
                start = idxs[k][bisect_left(idxs[k],start)]+1
            if flag:
                ans += 1
        return ans
                
                
            
            