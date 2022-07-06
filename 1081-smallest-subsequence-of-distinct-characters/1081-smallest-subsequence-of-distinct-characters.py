class Solution:
    def smallestSubsequence(self, s: str) -> str:
        dic = defaultdict(int)
        for i in range(len(s)):
            dic[s[i]] = i
        stack = []
        check = set()
        for i in range(len(s)):
            if s[i] in check:
                continue
            while stack and s[i]<=s[stack[-1]] and dic[s[stack[-1]]]>=i:
                check.remove(s[stack.pop()])
            check.add(s[i])
            stack.append(i)
        ans = ''
        for i in stack:
            ans += s[i]
        return ans
                
            