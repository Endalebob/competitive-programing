class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #I'm going to check if I start from this index I get positive
        # results if not I check the next index
        # if I didn't get I return -1
        ans = 0
        curr_n = 0
        curr_p = 0
        for i in range(len(gas)):
            curr_n += (gas[i]-cost[i])
            curr_p += (gas[i]-cost[i])
            if curr_p < 0:
                curr_p = 0
                ans = i+1
        return ans if (ans < len(gas)) and curr_n >= 0 else -1
            
        
        