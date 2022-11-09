class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dic = Counter(nums)
        ans = []
        for i in dic:
            if dic[i] == 1:
                ans.append(i)
        return ans