class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = {'a':0,'b':0,'c':0}
        ans = 0
        l = 0
        for i in range(len(s)):
            dic[s[i]] += 1
            while all(dic.values()):
                ans += len(s)-i
                dic[s[l]]-=1
                l += 1
        return ans
            