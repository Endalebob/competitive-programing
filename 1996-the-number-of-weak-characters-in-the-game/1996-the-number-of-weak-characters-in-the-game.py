class Solution:
    def numberOfWeakCharacters(self, p: List[List[int]]) -> int:
        val = sorted(p, key = lambda i: (-i[0],i[1]))
        count,ma = 0,0
        for i in val:
            if i[1]<ma: count += 1
            else: ma = i[1]
        return count