class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        digits = {
            '0': '',
            '1': 'One ',
            '2': 'Two ',
            '3': 'Three ',
            '4': 'Four ',
            '5': 'Five ',
            '6': 'Six ',
            '7': 'Seven ',
            '8': 'Eight ',
            '9': 'Nine '
        }
        
        tens = {
            '0': '',
            '2': 'Twenty ',
            '3': 'Thirty ',
            '4': 'Forty ',
            '5': 'Fifty ',
            '6': 'Sixty ',
            '7': 'Seventy ',
            '8': 'Eighty ',
            '9': 'Ninety '
        }
        
        teens = {
            '10': 'Ten ',
            '11': 'Eleven ',
            '12': 'Twelve ',
            '13': 'Thirteen ',
            '14': 'Fourteen ',
            '15': 'Fifteen ',
            '16': 'Sixteen ',
            '17': 'Seventeen ',
            '18': 'Eighteen ',
            '19': 'Nineteen '
        }
        last = ['','Thousand ','Million ','Billion ']
        numb = str(num)
        def rec(nums,turn):
            i = 0
            ret = ''
            flag = False
            one = ''
            two = ''
            tree = ''
            one = digits[nums[i]]
            i+=1
            if i < len(nums):
                if nums[i] == '1':
                    one = ''
                    two = teens[nums[i]+nums[i-1]]
                else:
                    two = tens[nums[i]]
            i+= 1
            if i<len(nums):
                if nums[i] != '0':
                    tree = digits[nums[i]] + 'Hundred '
            val = tree + two+  one
            if val != '':
                val += last[turn]
            return val
        nums = str(num)
        nums = nums[::-1]
        l,r = 0,3
        ans = ''
        j = 0
        while r<=len(nums):
            ans = rec(nums[l:r],j) + ans
            j+= 1
            l = r
            r += 3
        if l < len(nums):
            ans = rec(nums[l:len(nums)],j) + ans
        return ans.strip()
            
        
                    
                
        
        