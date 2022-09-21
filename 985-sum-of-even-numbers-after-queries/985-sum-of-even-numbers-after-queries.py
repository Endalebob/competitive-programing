class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evenSum = 0
        ans = []
        for i in nums:
            if i%2 == 0:
                evenSum += i
        for i in queries:
            if nums[i[1]] % 2 == 0:
                evenSum -= nums[i[1]]
            nums[i[1]] += i[0]
            if nums[i[1]] % 2 == 0:
                evenSum += nums[i[1]]
            ans.append(evenSum)
        return ans