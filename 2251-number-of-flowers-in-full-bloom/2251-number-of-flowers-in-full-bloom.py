class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        pre_sum = defaultdict(int)
        for i,j in flowers:
            pre_sum[i] += 1
            pre_sum[j+1] -= 1
        keys = sorted(pre_sum.keys())
        for i in range(1,len(keys)):
            pre_sum[keys[i]] += pre_sum[keys[i-1]]
        ans = []
        print(pre_sum[keys[-1]])
        for i in people:
            idx = bisect_right(keys,i)
            ans.append(pre_sum[keys[idx-1]])
        return ans
        
        