class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        ans = 0
        for i in range(len(num1)):
            c = int(num1[i])
            curr = 0
            for j in range(len(num2)):
                curr += (c*int(num2[j]))*(10**(i+j))
            ans += curr
        return str(ans)
        