class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = ''
        say = self.countAndSay(n-1)
        l,r = 0,0
        while r<len(say):
            r += 1
            if r<len(say) and say[r] != say[l]:
                s += str(r-l)
                s += say[l]
                l = r
        if r>l:
            s += str(r-l)
            s += say[l]
        return s
        # return rec(n)
                    
                    