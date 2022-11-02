class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        suff_sum = [0]
        for i in shifts[::-1]:
            suff_sum.append(suff_sum[-1]+i)
        suff_sum = suff_sum[::-1]
        return ''.join([chr(((ord(s[i])+suff_sum[i])-97)%26 + 97) for i in range(len(s))])
        