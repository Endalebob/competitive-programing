class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []
        nums = [i for i in range(1,n+1)]
        def comb(idx,temp):
            if len(temp) == k:
                combinations.append(temp[:])
                return
            if idx>=n:
                return
            comb(idx+1,temp)
            temp.append(nums[idx])
            comb(idx+1,temp)
            temp.pop()
        comb(0,[])
        return combinations
            