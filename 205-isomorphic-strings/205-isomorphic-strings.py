class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        dics = defaultdict(set)
        for i in range(len(t)):
            dict[i] = t[i]
        for i in range(len(s)):
            dics[s[i]].add(i)
        mapped = set()
        for i in dics:
            temp = set()
            for j in dics[i]:
                temp.add(t[j])
                hold = t[j]
                if t[j] in mapped:
                    return False
            if len(temp)>1:
                return False
            mapped.add(hold)
        return True