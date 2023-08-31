class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        new_arr = []
        for i in range(len(ranges)):
            if ranges[i]:
                new_arr.append((max(0,i-ranges[i]),min(n,i+ranges[i])))
        new_arr.sort(key=lambda x:(x[0],-x[1]))
        end = 0
        ans = 0
        i = 0
        while i<len(new_arr):
            temp = end
            while i<len(new_arr) and new_arr[i][0]<=end:
                temp = max(temp,new_arr[i][1])
                i += 1
            if temp == end:
                return -1
            if temp == n:
                return ans+1
            end = temp
            ans += 1
        return -1
            