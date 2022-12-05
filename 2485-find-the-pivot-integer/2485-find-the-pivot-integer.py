class Solution:
    def pivotInteger(self, n: int) -> int:
        piv = [1]
        pv = [n]
        for i in range(2,n+1):
            piv.append(piv[-1]+i)
            pv.append(pv[-1]+n-i+1)
        for i in range(len(piv)):
            if piv[i]==pv[-i-1]:
                return i+1
        return -1