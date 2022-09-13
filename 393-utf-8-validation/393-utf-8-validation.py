class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        i = 0
        print(format(250,'b'))
        print(format(145,'b'))
        while i<len(data):
            temp = 1
            if data[i] & (1<<7):
                while temp<8 and data[i] &(1<<(7-temp)):
                    temp += 1
            else:
                i += 1
                continue
            if temp == 1 or temp>4:
                    return False
            elif i+temp>len(data):
                return False
            for ii in range(1,temp):
                if not (data[i+ii] &(1<<7)) or (data[i+ii] &(1<<6)):
                    return False
            i += temp
        return True