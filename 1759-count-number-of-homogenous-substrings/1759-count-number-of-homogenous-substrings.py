class Solution:
    def countHomogenous(self, s: str) -> int:
        new_arr = []
        cur = 1
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                new_arr.append(cur)
                cur = 1
            else:
                cur += 1
        new_arr.append(cur)
        print(new_arr)
        return sum([(i**2+i)//2 for i in new_arr])%(10**9+7)