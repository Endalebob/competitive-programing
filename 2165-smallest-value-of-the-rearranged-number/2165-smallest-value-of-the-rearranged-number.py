class LessThan(str):
    def __lt__(a,b):
        return a+b > b+a
class GreaterThan(str):
    def __gt__(a,b):
        return a+b>b+a
class Solution:
    def smallestNumber(self, num: int) -> int:
        num = str(num)
        if num[0] == '-':
            large_num = ''.join(sorted(num[1:],key = LessThan))
            large_num = '-' + large_num
        else:
            large_num = ''.join(sorted(num,key = GreaterThan))
        if large_num[0] == '0':
            lis = list(large_num)
            for i in range(len(str(large_num))):
                if lis[i] != '0':
                    lis[i],lis[0] = lis[0],lis[i]
                    break
            return int(''.join(lis))
        return int(large_num)