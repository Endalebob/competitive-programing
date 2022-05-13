class Solution:
    def reverseBits(self, n: int) -> int:
        binary = str(bin(n))[2:]
        ans = (32-len(binary))*'0' + binary
        return int(ans[::-1],2)