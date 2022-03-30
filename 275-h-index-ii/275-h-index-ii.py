class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = citations[::-1]
        right = len(citations)-1
        left = 0
        mid = (right + left)//2
        if len(citations) == 1 and citations[0] <= 0:
            return 0
        if len(citations) == 1:
            return 1
        ans = 0
        while left<right:
            if citations[mid] >= mid+1:
                left = mid+1
                ans = mid+1
                mid = (right + left)//2
            else:
                right = mid-1
                mid = (right + left)//2
        if citations[mid] >= mid+1:
                ans = mid+1
        return ans
    
            