class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        counter = Counter(p)
        len_p = len(p)
        ans = []
        compare = Counter(s[:len_p])
        if compare == counter:
            ans.append(0)
        for i in range(1,len(s)-len_p+1):
            compare[s[i-1]] -= 1
            compare[s[i+len_p-1]] += 1
            if compare == counter:
                ans.append(i)
        return ans