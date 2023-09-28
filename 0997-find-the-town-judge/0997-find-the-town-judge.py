class Solution:
    def findJudge(self, n: int, t: List[List[int]]) -> int:
        if n==1 and not t:
            return 1
        trust = defaultdict(set)
        trusted = defaultdict(set)
        for i,j in t:
            trust[i].add(j)
            trusted[j].add(i)
        for i in trusted:
            if i not in trust and len(trusted[i]) == n-1:
                return i
        return -1
        