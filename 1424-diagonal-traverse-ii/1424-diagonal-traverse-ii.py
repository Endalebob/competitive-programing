class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        col = 0
        dic = defaultdict(list)
        for i in range(len(nums)-1,-1,-1):
            col = max(col,len(nums[i]))
            for j in range(len(nums[i])):
                dic[i+j].append(nums[i][j])
        ans = []
        is_valid = lambda r,c : 0<=r<len(nums) and 0<=c<col
        def travers(i,j):
            for num in dic[i+j]:
                ans.append(num)
        for row in range(len(nums)-1):
            travers(row,0)
        for j in range(col):
            travers(len(nums)-1,j)
        return ans
        