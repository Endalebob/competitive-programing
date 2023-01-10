class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        aa = num % 3
        a = num // 3
        
        if aa == 0:
            return [a-1,a,a+1]
        return []
            