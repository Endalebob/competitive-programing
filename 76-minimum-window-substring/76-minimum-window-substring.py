class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r,start,end,flag = 0,-1,0,len(s) + 1,len(t)
        dic = Counter(t)
        while r<len(s)-1 or flag == 0:
            if flag != 0:
                r += 1
                if s[r] in dic:
                    dic[s[r]] -= 1
                    if dic[s[r]] >= 0:
                        flag -= 1
                    
                    
            else:
                if r-l<end-start:
                    end = r
                    start = l
                if s[l] in dic:
                    dic[s[l]] += 1
                    if dic[s[l]] > 0:
                        flag += 1
                l += 1
        if end > len(s):
            return ''
        return s[start:end+1]