class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        checker = defaultdict(set)
        checker2 = defaultdict(set)
        for i in range(len(s)):
            checker[s[i]].add(t[i])
            checker2[t[i]].add(s[i])
            if len(checker[s[i]]) > 1 or len(checker2[t[i]]) > 1:
                return False
        return True
        