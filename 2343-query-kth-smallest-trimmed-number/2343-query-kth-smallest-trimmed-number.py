class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        for a,(i,j) in enumerate(queries):
            temp = []
            c = a
            for k in range(len(nums)):
                temp.append([nums[k][-j:],c,k])
                c += 1
            temp.sort()
            ans.append(temp[i-1][2])
        return ans