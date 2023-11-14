class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        diff = defaultdict(list)
        for i in range(len(s)):
            diff[s[i]].append(i)
        val = ord('a')
        ans = 0
        for i in diff:
            if len(diff[i]) < 2:
                continue
            if diff[i][-1] - diff[i][0] > 1:
                for ii in range(26):
                    let = chr(val+ii)
                    if let in diff:
                        left = bisect_right(diff[let],diff[i][0])
                        right = bisect_left(diff[let],diff[i][-1])
                        ans += (right>left)
        return ans
        