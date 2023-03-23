class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        pref_sum = [ord(i) for i in s]
        start = defaultdict(int)
        end = defaultdict(int)
        for l,r,flag in shifts:
            if flag:
                start[l] += 1
                start[r+1] -= 1
            else:
                start[l] -= 1
                start[r+1] += 1
        current = 0
        for i in range(len(s)):
            current += (start[i])
            pref_sum[i] += current
        return ''.join([chr((i-97)%26 + 97) for i in pref_sum])
            
            
                