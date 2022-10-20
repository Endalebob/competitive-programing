class Solution:
    def intToRoman(self, num: int) -> str:
        iTr = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
        special_case = {4:'IV',9:'IX',40:'XL',90:'XC',400:'CD',900:'CM'}
        def separate_digit(digit):
            len_ = len(str(digit))-1
            ans = []
            while len_:
                ans.append((digit//(10**len_)) * 10**len_)
                digit %= 10**len_
                len_ -= 1
            ans.append(digit)
            return ans
        ans = ''
        key = sorted(iTr.keys(),reverse = True)
        for i in separate_digit(num):
            if i in special_case:
                ans += special_case[i]
            else:
                for j in key:
                    if j <= i:
                        ans += (iTr[j]*(i//j))
                        i -= (j*(i//j))
        return ans
                    
            