class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        fib = [1,1]
        while fib[-1]<=k:
            fib.append(fib[-1]+fib[-2])
        fib.pop()
        i = len(fib)-1
        ans = 0
        while k != 0:
            if fib[i] <= k:
                ans += 1
            k = k%fib[i]
            i -= 1
        return ans