class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        comb = [[i,j] for i,j in zip(growTime,plantTime)]
        comb.sort(reverse = True)
        start = 0
        ans = 0
        for i in comb:
            ans = max(ans,start+i[1]+i[0])
            start += i[1]
        return ans