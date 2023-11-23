class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i in range(len(l)):
            if l[i]-r[i] == 1:
                ans.append(True)
            else:
                num = sorted(nums[l[i]:r[i]+1])
                dif = num[1]-num[0]
                flag = True
                for i in range(1,len(num)):
                    if dif != num[i]-num[i-1]:
                        flag = False
                        break
                ans.append(flag)
        return ans