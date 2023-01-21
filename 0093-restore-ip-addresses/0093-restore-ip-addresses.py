class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        vstd = set()
        def back(cnt,idx,s):
            if cnt == 0:
                if s in vstd:
                    return
                new = s.split('.')
                for i in new:
                    if ((len(i) == 3) and i > '255') or len(i) > 3 or (len(i)>1 and i[0] == '0') or not i:
                        return
                vstd.add(s)
                ans.append('.'.join(new))
                return
            for i in range(idx+1,idx+4):
                new = s[:i] + '.' + s[i:]
                back(cnt-1,i+1,new)
            return ans
        return back(3,0,s)