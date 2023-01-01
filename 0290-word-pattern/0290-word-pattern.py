class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        new_year = s.split()
        dic = defaultdict(set)
        dicc = defaultdict(set)
        if len(new_year) != len(pattern):
            return False
        for i in range(len(pattern)):
            dic[pattern[i]].add(new_year[i])
            dicc[new_year[i]].add(pattern[i])
            if len(dic[pattern[i]]) > 1 or len(dicc[new_year[i]])>1:
                return False
        return True