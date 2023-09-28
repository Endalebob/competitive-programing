class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        repeat = set()
        l=r=0
        while r<len(s):
            while s[r] in repeat:
                repeat.remove(s[l])
                l += 1
            repeat.add(s[r])
            ans = max(ans,len(repeat))
            r += 1
        return ans
        