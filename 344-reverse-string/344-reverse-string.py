class Solution:
    def reve(self,s,i,j):
        if i>=j: return s
        s[i],s[j]=s[j],s[i]
        return self.reve(s,i+1,j-1)
    def reverseString(self, s: List[str]) -> None:
        self.reve(s,0,len(s)-1)
        