class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = defaultdict(int)
        add = defaultdict(int)
        for i in range(n//2):
            a = [nums[i],nums[-1-i]]
            add[sum(a)] += 1
            mi,ma = min(a),max(a)
            diff[mi+1] -= 1
            diff[ma+limit+1] += 1
        ans = float('inf')
        curr = n
        for i in range(2,2*limit+1):
            curr += diff[i]
            ans = min(curr-add[i],ans)
        return ans