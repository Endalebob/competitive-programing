class Solution:
    def reorderedPowerOf2(self, m: int) -> bool:
        n = 1
        ans = set()
        while n<10**9:
            a = n
            n *= 2
            ans.add(a)
        vals = list(permutations(str(m)))
        for i in vals:
            temp = ''.join(i)
            if temp[0] == '0':
                continue
            if int(temp) in ans:
                return True
        return False