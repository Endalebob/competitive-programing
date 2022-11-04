class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        prime = [1]*(n)
        for j in range(2,int(n**0.5)+1):
            if prime[j] == 0:
                continue
            for i in range(j*j,n,j):
                prime[i] = 0
        return prime.count(1)-2