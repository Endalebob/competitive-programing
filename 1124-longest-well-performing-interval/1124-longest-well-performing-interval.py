class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        
        
        #go by creating prefix_sum if it is postive add upto index
        #else check is there any other number less than current if exit update
        
        dic = {}
        score = ans = 0
        
        
        for i,v in enumerate(hours):
            score = score + 1 if v>8 else score - 1
            
            if score > 0:
                ans = i+1
            elif score not in dic:
                dic[score] = i
            if score-1 in dic:
                ans = max(ans,i-dic[score-1])
        
        return ans