class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        ans = 0
        for i in range(len(citations)):
            if citations[-i-1]>=i+1:
                ans +=1
                continue
            return ans
        return ans
        