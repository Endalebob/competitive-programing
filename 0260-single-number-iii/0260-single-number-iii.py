class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for i in nums:
            xor ^= i
        last_bit_of_xor = xor & (xor-1) ^ xor
        n1 = 0
        for i in nums:
            if last_bit_of_xor & i:
                n1 ^= i
        return n1,n1^xor