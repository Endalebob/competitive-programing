class Solution:
    def maximumSwap(self, num: int) -> int:
        snum = list(str(num))
        ans = num
        for i in range(len(snum)-1):
            for j in range(i+1,len(snum)):
                if snum[i] < snum[j]:
                    snum[i],snum[j] = snum[j],snum[i]
                    new_num = int(''.join(snum))
                    ans = max(ans,new_num)
                    snum[i],snum[j] = snum[j],snum[i]
        return ans
                    
        