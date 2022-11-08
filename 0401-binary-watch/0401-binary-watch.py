class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        for i in range(12):
            count_hr_bit = format(i,'b').count('1')
            if count_hr_bit > turnedOn:
                continue
            for j in range(60):
                count_min_bit = format(j,'b').count('1')
                if count_min_bit + count_hr_bit == turnedOn:
                    minute = str(j).zfill(2)
                    ans.append(str(i)+':' + minute)
        return ans
        