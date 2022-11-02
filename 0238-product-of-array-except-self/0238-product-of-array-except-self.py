class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeros_index = -1
        product = 1
        count = 0
        for index,num in enumerate(nums):
            if num == 0:
                count +=1
                zeros_index = index
            else:
                product *=num
        
        if count > 1:
            return [0 for _ in range(len(nums))]
        
        if count == 1:
            return [0 if index != zeros_index else product for index in range(len(nums))]
        
        output = []
        
        for num in nums:
            tempo_res = 0
            devidend = abs(product)
            devisor = abs(num)
            
            while devidend:
                multiplier = 1
                
                while devidend - multiplier * devisor >= 0:
                    tempo_res += multiplier
                    devidend -= multiplier*devisor
                    multiplier *=2
            if num < 0 and product < 0 or num > 0 and product > 0:
                output.append(tempo_res)
            else:
                output.append(-tempo_res)
            
        
        return output
                
            
                
                
        
        
        
                