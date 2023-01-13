class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        '''
        first I create an array of positive and negative numbers,
        then I take elements from them one by one.
        '''
        pos = [i for i in nums if i>0]
        neg = [i for i in nums if i<0]
        ans = []
        for i in range(len(neg)):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans
                
        