class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left,right = 0,0
        count = defaultdict(int)
        maxx,ans = 0,0
        while right<len(s):
            count[s[right]]+=1
            maxx = max(maxx,count[s[right]])
            if maxx+left+k > right:
                ans = max(ans,right-left+1)
            else:
                count[s[left]]-=1
                left += 1
            right += 1
        return ans