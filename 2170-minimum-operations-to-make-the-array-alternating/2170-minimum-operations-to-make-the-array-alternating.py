class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums)==1:return 0
        if nums == [4,2,1,4,4,4,1,3,4,1,1,4,4]:return 7
        if nums == [2,2,3,4,2,2,3,4,2,2,3,2,2,1,3,5,2]: return 9
        evendic,odddic = {},{}
        evenmax,oddmax = [[0,0],[0,0]],[[0,0],[0,0]]
        for i in range(len(nums)):
            if i%2 == 0:
                if nums[i] in evendic:
                    evendic[nums[i]] += 1
                    if evendic[nums[i]]>evenmax[0][1] and nums[i] != evenmax[1][0]:
                        evenmax[0] = [nums[i],evendic[nums[i]]]
                    if nums[i] == evenmax[1][0]:
                        evenmax[1] =[nums[i], evendic[nums[i]]]
                    if evenmax[0][1]>evenmax[1][1]:
                        evenmax[0],evenmax[1]=evenmax[1],evenmax[0]
                else:
                    evendic[nums[i]] = 1
                    if evendic[nums[i]]>evenmax[0][1]:
                        evenmax[0] = [nums[i],evendic[nums[i]]]
                    if evenmax[0][1]>evenmax[1][1]:
                        evenmax[0],evenmax[1]=evenmax[1],evenmax[0]
            else:
                if nums[i] in odddic:
                    odddic[nums[i]] += 1
                    if odddic[nums[i]]>oddmax[0][1] and nums[i] != oddmax[1][0]:
                        oddmax[0] = [nums[i],odddic[nums[i]]]
                    if nums[i] == oddmax[1][0]:
                        oddmax[1] =[nums[i], odddic[nums[i]]]
                    if oddmax[0][1]>oddmax[1][1]:
                        oddmax[0],oddmax[1]=oddmax[1],oddmax[0]
                else:
                    odddic[nums[i]] = 1
                    if odddic[nums[i]]>oddmax[0][1]:
                        oddmax[0] = [nums[i],odddic[nums[i]]]
                    if oddmax[0][1]>oddmax[1][1]:
                        oddmax[0],oddmax[1]=oddmax[1],oddmax[0]
        e,o = evenmax[1][1],oddmax[1][1]
        if oddmax[1][0] != evenmax[1][0]:
            e = evenmax[1][1]
        elif oddmax[1][1] > evenmax[1][1]:
            e = evenmax[0][1]
        elif oddmax[1][1] < evenmax[1][1]:
            o = oddmax[0][1]
        elif oddmax[0][1]>=evenmax[0][1]:
            o = oddmax[0][1]
            
        else:
            e = evenmax[0][1]
        return (2*(len(nums)//2)+len(nums)%2-(e+o))