class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        sumUpToNow = 0
        count = 0
        mod = (10**9+7)
        prefixes = defaultdict(int)
        prefixes[0] = 1
        
        for i in range(len(arr)):
            sumUpToNow += arr[i]
            rem = sumUpToNow % 2
            count += prefixes[rem]
            # count %= mod
            prefixes[rem] += 1
            
        totalSum = (len(arr) * (len(arr) + 1)) // 2
        
        return (totalSum - count) % mod
         
        